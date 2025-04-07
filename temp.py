
import requests

# Define the API endpoint
url = "https://www.producthunt.com/frontend/graphql"

# Define the request headers
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

# Define the payload
payload = {
    "operationName": "ProductsPageLayout",
    "variables": {
        "slug": "coderabbit-2"
    },
    "extensions": {
        "persistedQuery": {
            "version": 1,
            "sha256Hash": "159f1cff8868f1f6afd4de0f40338d6ab826bd8bf51d6305ce0ddf3b23ad3e9a"
        }
    }
}

# Make the POST request
response = requests.post(url, json=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extracting information from the response and assigning to variables
    product_data = data['data']['product']

    product_id = product_data['id']
    product_name = product_data['name']
    tagline = product_data['tagline']
    reviews_count = product_data['reviewsCount']
    reviews_rating = product_data['reviewsRating']
    followers_count = product_data['followersCount']
    website_url = product_data['websiteUrl']
    product_url = product_data['url']
    is_no_longer_online = product_data['isNoLongerOnline']
    is_claimed = product_data['isClaimed']
    is_top_product = product_data['isTopProduct']
    github_url = product_data['githubUrl']
    twitter_url = product_data['twitterUrl']
    linkedin_url = product_data['linkedinUrl']
    instagram_url = product_data['instagramUrl']
    facebook_url = product_data['facebookUrl']
    angellist_url = product_data['angellistUrl']
    can_edit = product_data['canEdit']
    logo_uuid = product_data['logoUuid']
    featured_shoutouts_to_count = product_data['featuredShoutoutsToCount']
    shoutouts_to_count = product_data['shoutoutsToCount']
    badges_count = product_data['badges']['totalCount']
    slug = product_data['slug']
    is_maker = product_data['isMaker']
    addons_count = product_data['addonsCount']
    is_subscribed = product_data['isSubscribed']
    is_muted = product_data['isMuted']
    clean_url = product_data['cleanUrl']
    ios_url = product_data['iosUrl']
    android_url = product_data['androidUrl']
    threads_url = product_data['threadsUrl']
    medium_url = product_data['mediumUrl']

    # Extract makers
    makers = [maker['node']['name'] for maker in product_data['makers']['edges']]

    # Extract upcoming banner followers
    upcoming_banner_followers = []
    if 'upcomingBannerFollowers' in product_data:
        upcoming_banner_followers = [
            follower['node']['name'] for follower in product_data['upcomingBannerFollowers']['edges']
        ]

    # Extract awards
    awards = []
    if 'awards' in product_data:
        awards = [
            award['node']['post']['name'] for award in product_data['awards']['edges']
        ]

    # Extract discussion forum details
    discussion_forum = product_data.get('discussionForum', {})
    discussion_threads = []
    if 'threads' in discussion_forum:
        discussion_threads = [
            thread['node']['title'] for thread in discussion_forum['threads']['edges']
        ]

    # Print extracted information
    print(f"Product ID: {product_id}")
    print(f"Product Name: {product_name}")
    print(f"Tagline: {tagline}")
    print(f"Reviews Count: {reviews_count}")
    print(f"Reviews Rating: {reviews_rating}")
    print(f"Followers Count: {followers_count}")
    print(f"Website URL: {website_url}")
    print(f"Product URL: {product_url}")
    print(f"Is No Longer Online: {is_no_longer_online}")
    print(f"Is Claimed: {is_claimed}")
    print(f"Is Top Product: {is_top_product}")
    print(f"GitHub URL: {github_url}")
    print(f"Twitter URL: {twitter_url}")
    print(f"LinkedIn URL: {linkedin_url}")
    print(f"Instagram URL: {instagram_url}")
    print(f"Facebook URL: {facebook_url}")
    print(f"AngelList URL: {angellist_url}")
    print(f"Can Edit: {can_edit}")
    print(f"Logo UUID: {logo_uuid}")
    print(f"Featured Shoutouts Count: {featured_shoutouts_to_count}")
    print(f"Shoutouts Count: {shoutouts_to_count}")
    print(f"Badges Count: {badges_count}")
    print(f"Slug: {slug}")
    print(f"Is Maker: {is_maker}")
    print(f"Addons Count: {addons_count}")
    print(f"Is Subscribed: {is_subscribed}")
    print(f"Is Muted: {is_muted}")
    print(f"Clean URL: {clean_url}")
    print(f"iOS URL: {ios_url}")
    print(f"Android URL: {android_url}")
    print(f"Threads URL: {threads_url}")
    print(f"Medium URL: {medium_url}")
    print(f"Makers: {', '.join(makers)}")
    print(f"Upcoming Banner Followers: {', '.join(upcoming_banner_followers)}")
    print(f"Awards: {', '.join(awards)}")
    print(f"Discussion Threads: {', '.join(discussion_threads)}")
