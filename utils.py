import requests
import logging
import re
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
                'slug': node.get('slug'),
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

def get_product_details(client, slug):
    """Fetch product details by slug."""
    payload = {
        "operationName": "ProductsPageLayout",
        "variables": {"slug": slug},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "159f1cff8868f1f6afd4de0f40338d6ab826bd8bf51d6305ce0ddf3b23ad3e9a",
            }
        },
    }

    data = client.post(payload)
    if not data:
        return {}

    product = data.get("data", {}).get("product", {})
    return {
        "id": product.get("id"),
        "name": product.get("name"),
        "tagline": product.get("tagline"),
        "reviews_count": product.get("reviewsCount"),
        "reviews_rating": product.get("reviewsRating"),
        "followers_count": product.get("followersCount"),
        "website_url": product.get("websiteUrl"),
        "product_url": product.get("url"),
        "github": product.get("githubUrl"),
        "twitter": product.get("twitterUrl"),
        "linkedin": product.get("linkedinUrl"),
        "instagram": product.get("instagramUrl"),
        "facebook": product.get("facebookUrl"),
        "angellist": product.get("angellistUrl"),
        "badges_count": product.get("badges", {}).get("totalCount", 0),
        "makers": [maker["node"]["name"] for maker in product.get("makers", {}).get("edges", [])],
    }


def get_product_comments(client, slug):
    """Fetch top comments from the product page."""
    payload = {
        "operationName": "PostPageComments",
        "variables": {
            "commentsListSubjectThreadsCursor": "",
            "commentsThreadRepliesCursor": "",
            "order": "VOTES",
            "slug": slug,
            "includeThreadForCommentId": None,
            "commentsListSubjectThreadsLimit": 4,
            "commentsListSubjectFilter": None,
            "excludeThreadForCommentId": None,
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "30f2a3c9af5dce9b7e8cbe7b8ad23bd4bc6eda38a9d69a88e247e6c1efd08442",
            }
        },
    }

    data = client.post(payload)
    if not data:
        return []

    comments = data.get("data", {}).get("post", {}).get("threads", {}).get("edges", [])
    extracted_comments = []

    for comment in comments:
        node = comment.get("node", {})
        if node.get("isSticky") and "maker" in node.get("badges", []):
            body = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>([^<]+)</a>', r'\1', node["body"])
            extracted_comments.append({
                "user": node["user"]["name"],
                "username": node["user"]["username"],
                "comment": body,
                "url": node["url"],
            })
    
    return extracted_comments


def get_product_about(client, slug):
    """Fetch additional product information."""
    payload = {
        "operationName": "ProductAboutPage",
        "variables": {"productSlug": slug},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "c7495797778b271a67f42cc2709ed506dea300938c11173729e5266432732643",
            }
        },
    }

    data = client.post(payload)
    if not data:
        return {}

    product = data.get("data", {}).get("product", {})
    return {
        "id": product.get("id"),
        "slug": product.get("slug"),
        "name": product.get("name"),
        "description": product.get("description"),
        "reviews_count": product.get("reviewsCount"),
        "reviews_rating": product.get("reviewsRating"),
        "stacks_count": product.get("stacksCount"),
        "posts_count": product.get("postsCount"),
        # "categories": [category["node"]["name"] for category in product.get("categories", {}).get("edges", [])],
        "categories": [category["title"] for category in product.get("categories", []) if isinstance(category, dict)],

    }


def get_full_product_info(client, slug):
    """Wrapper function to merge all product details, comments, and about info."""
    product_details = get_product_details(client, slug)
    product_comments = get_product_comments(client, slug)
    product_about = get_product_about(client, slug)

    return {
        "product_details": product_details,
        "product_comments": product_comments,
        "product_about": product_about,
    }
