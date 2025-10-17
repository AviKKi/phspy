import requests
import argparse
import logging
import re
from time import sleep
from datetime import datetime, timedelta
from urllib.parse import urlencode

logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s")

def parse_args():
    parser = argparse.ArgumentParser(description='Product Hunt Crawler')
    parser.add_argument('--start_date', required=True, help='Start date in YYYY-MM-DD format')
    parser.add_argument('--end_date', required=True, help='End date in YYYY-MM-DD format')
    return parser.parse_args()

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
        # self.headers = {
        #     'Content-Type': 'application/json',
        #     'Referer': 'https://www.producthunt.com/',
        #     "Origin": "https://www.producthunt.com",
        #     # 'User-Agent': 'Mozilla/5.0'
        #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
        # }
        self.headers = {
            'accept': '/',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.producthunt.com/',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            'x-ph-referer': '',
            'x-ph-timezone': 'Asia/Calcutta',
            'x-requested-with': 'XMLHttpRequest',
        }
        self.max_tries = max_tries
        self.timeout = timeout

    def post(self, payload):
        for attempt in range(self.max_tries):
            try:
                response = requests.post(self.BASE_URL, headers = self.headers, json = payload, timeout = self.timeout)
                sleep(2)

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
                    'sha256Hash': 'ce32fb1aebe25a692312819733730b73176df680396413607ae6811f446850c9'
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
            
            redirect_to_product = node.get('redirectToProduct')
            slug = redirect_to_product.get('slug') if redirect_to_product else node.get('slug')
            all_products.append({
                'name': node.get('name'),
                'slug': slug,
                'votes': node.get('votesCount'),
                'launch_date': node.get('createdAt'),
                'topics': [topic['node']['name'] for topic in node.get('topics', {}).get('edges', [])],
                'product_url': f"https://www.producthunt.com/{node.get('shortenedUrl')}",
                'comments_count': node.get('commentsCount'),
                'product_id_on_PH': node.get('id'),
                'latest_score': node.get('latestScore'),
                'launch_day_score': node.get('launchDayScore')
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
                "sha256Hash": "0bc0a15a95f37395ab7e2a7df5c8f96f85d8dd5fafa63c8679b053096c967eba",
            }
        },
    }
    print(f" collecting data for {slug}")
    data = client.post(payload)
    # print(f"Raw data for {slug}: {data}")
    if not data:
        return {}

    product = data.get("data", {}).get("product", {})
    print(f" data collected for {slug}")
    # print("DEBUG: product raw data:", data)
    return {
        "id": product.get("id"),
        "slug": product.get("slug"),
        "name": product.get("name"),
        "tagline": product.get("tagline"),
        # "reviews_count": product.get("reviewsCount"),
        # "reviews_rating": product.get("reviewsRating"),
        "followers_count": product.get("followersCount"),
        "website_url": product.get("websiteUrl"),
        "product_url_on_PH": product.get("url"),
        "github": product.get("githubUrl"),
        "twitter": product.get("twitterUrl"),
        "linkedin": product.get("linkedinUrl"),
        "instagram": product.get("instagramUrl"),
        "facebook": product.get("facebookUrl"),
        "angellist": product.get("angellistUrl"),
        "android_url": product.get("androidUrl"),
        "clean_url": product.get("cleanUrl"),
        "ios_url": product.get("iosUrl"),
        "medium_url": product.get("mediumUrl"),
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
                "sha256Hash": "a3fe1abceecfe7e57d669246ae95b88483d50b9ff511359fc6bea2670b019677",
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
            extracted_comments.append( {
                "slug": slug,
                "main_comment_by_user": node["user"]["name"],
                "main_comment_username": node["user"]["username"],
                "main_comment": body,
                "main_comment_url": node["url"],
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
                "sha256Hash": "a5175e257a694ebba472b4fa5a570e308e808b05fd65d6279bccc49012a888fe",
            }
        },
    }

    data = client.post(payload)
    if not data:
        return {}

    product = data.get("data", {}).get("product", {})
    return {
        # "id": product.get("id"),
        "slug": product.get("slug"),
        # "name": product.get("name"),
        "description": product.get("description"),
        "reviews_count": product.get("reviewsCount"),
        "reviews_rating": product.get("reviewsRating"),
        "stacks_count": product.get("stacksCount"),
        "posts_count": product.get("postsCount"),
        # "categories": [category["node"]["name"] for category in product.get("categories", {}).get("edges", [])],
        "categories": [category["title"] for category in product.get("categories", []) if isinstance(category, dict)],
        "post_names": [post["node"]["name"] for post in product.get("posts", {}).get("edges", [])],
        "post_slugs": [post["node"]["slug"] for post in product.get("posts", {}).get("edges", [])]

    }


# def get_full_product_info(client, slug):
#     """Wrapper function to merge all product details, comments, and about info."""
#     product_details = get_product_details(client, slug)
#     product_comments = get_product_comments(client, slug)
#     product_about = get_product_about(client, slug)

#     return {
#         "product_details": product_details,
#         "product_comments": product_comments,
#         "product_about": product_about,
#     }
