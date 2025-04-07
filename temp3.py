import requests

url = "https://www.producthunt.com/frontend/graphql"

headers = {
    "Content-Type": "application/json",
    "Referer": "https://www.producthunt.com/",
    "Origin": "https://www.producthunt.com",
    "User-Agent": "Mozilla/5.0"
}

payload = {
    "operationName": "ProductAboutPage",
    "variables": {
        "productSlug": "easystaff-payroll"
    },
    "extensions": {
        "persistedQuery": {
            "version": 1,
            "sha256Hash": "c7495797778b271a67f42cc2709ed506dea300938c11173729e5266432732643"
        }
    }
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()

    #extract required variables
    product = data["data"]["product"]
    product_id = product["id"]
    product_slug = product["slug"]
    product_name = product["name"]
    product_description = product["description"]
    reviews_count = product["reviewsCount"]
    reviews_rating = product["reviewsRating"]
    stacks_count = product["stacksCount"]
    posts_count = product["postsCount"]
    categories = [cat["title"] for cat in product["categories"]]
    post_names = [post["node"]["name"] for post in product["posts"]["edges"]]
    post_slugs = [post["node"]["slug"] for post in product["posts"]["edges"]]

    # Print extracted variables     
    print("Product Details:")
    print(f"ID: {product_id}")
    print(f"Slug: {product_slug}")
    print(f"Name: {product_name}")
    print(f"Description: {product_description}")
    print(f"Reviews Count: {reviews_count}")
    print(f"Reviews Rating: {reviews_rating}")
    print(f"Stacks Count: {stacks_count}")
    print(f"Posts Count: {posts_count}")
    print(f"Categories: {categories}")
    print(f"Post Names: {post_names}")
    print(f"Post Slugs: {post_slugs}")

else:
    print(f"Failed to fetch data: {response.status_code}")

