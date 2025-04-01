import requests
import logging
from time import sleep
from datetime import datetime, timedelta

logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s")

def generate_date_range(start_date: str, end_date: str):
    try:
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')

        if start > end:
            raise ValueError('start_date cannot be after end_date.')

        return [(start + timedelta(days = i)).strftime('%Y-%m-%d') for i in range((end - start).days + 1)]
    except ValueError as e:
        logging.error(f'Error generating date range: {e}')
        return []

class ProductHuntClient:
    BASE_URL = 'https://www.producthunt.com/frontend/graphql'

    def __init__(self, max_tries=3, timeout=10):
        self.headers = {
            'Content-Type': 'application/json',
            'Referer': 'https://www.producthunt.com/',
            'User-Agent': 'Mozilla/5.0'
        }
        self.max_tries = max_tries
        self.timeout = timeout

    def post(self, payload):
        for attempt in range(self.max_tries):
            try:
                response = requests.post(self.BASE_URL, headers = self.headers, json = payload, timeout = self.timeout)

                if response.status_code == 200:
                    logging.info('Request successful')
                    return response.json()
                elif 400 <= response.status_code < 500:
                    logging.error(f'Client Error {response.status_code}: {response.text}')
                    break
                elif 500 <= response.status_code < 600:
                    logging.warning(f'Server Error {response.status_code}, retrying...')
                    sleep(2)
            except requests.exceptions.Timeout:
                logging.warning('Request timed out. Retrying...')
            except requests.exceptions.RequestException as e:
                logging.error(f'Request failed: {e}')
                break
            
        return None

def get_products_on_date(client, year, month, day):
    cursor = None
    all_products = []

    while True:
        payload = {
            'operationName': 'LeaderboardDailyPage',
            'variables': {
                'featured': False,
                'year': year,
                'month': month,
                'day': day,
                'order': 'VOTES', # 'VOTES' or 'FEATURED' or 'DAILY_RANK'
                'cursor': cursor
            },
            'extensions': {
                'persistedQuery': {
                    'version': 1,
                    'sha256Hash': '026278149fa3f7dc43d81a35bda839586fbebf2d7206023cb31ea1d501f6e3d5'
                }
            }
        }

        data = client.post(payload)
        if not data:
            logging.error('Failed to retrieve data')
            break
        
        homefeed = data.get('data', {}).get('homefeedItems', {})
        products = homefeed.get('edges', [])

        for product in products:
            node = product.get('node', {})
            if node.get('__typename') == 'Ad':
                continue
            all_products.append({
                'name': node.get('name'),
                'tagline': node.get('tagline'),
                'votes': node.get('votesCount'),
                'launch_date': node.get('createdAt'),
                'topics': [topic['node']['name'] for topic in node.get('topics', {}).get('edges', [])],
                'product_url': f"https://www.producthunt.com/{node.get('shortenedUrl')}"
            })

        page_info = homefeed.get('pageInfo', {})
        has_next_page = page_info.get('hasNextPage', False)
        cursor = page_info.get('endCursor', None)

        if not has_next_page:
            break
        
    return all_products