import requests

url = "https://www.producthunt.com/frontend/graphql"
headers = {
    "Content-Type": "application/json",
    "Referer": "https://www.producthunt.com/",
    "User-Agent": "Mozilla/5.0"
}
payload = {
    "operationName": "PostPageComments",
    "variables": {
        "commentsListSubjectThreadsCursor": "",
        "commentsThreadRepliesCursor": "",
        "order": "VOTES",
        "slug": "easystaff-payroll",
        "includeThreadForCommentId": None,
        "commentsListSubjectThreadsLimit": 4,
        "commentsListSubjectFilter": None,
        "excludeThreadForCommentId": None
    },
    "extensions": {
        "persistedQuery": {
            "version": 1,
            "sha256Hash": "30f2a3c9af5dce9b7e8cbe7b8ad23bd4bc6eda38a9d69a88e247e6c1efd08442"
        }
    }
}

response = requests.post(url, json=payload, headers=headers)

import re

if response.status_code == 200:
    data = response.json()
    
    # Extract comments
    comments = data.get("data", {}).get("post", {}).get("threads", {}).get("edges", [])

    for comment in comments:
        node = comment.get("node", {})
        
        # Check if comment is sticky and written by maker
        if node.get("isSticky") and "maker" in node.get("badges", []):
            body = node["body"]

            # Remove HTML anchor tags while keeping the URL
            body = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>([^<]+)</a>', r'\1', body)

            print(f"Comment by {node['user']['name']} (@{node['user']['username']}):\n")
            print(body)
            print("\nURL:", node["url"])
            break  # Stop after finding the first pinned maker comment

else:
    print(f"Request failed with status code {response.status_code}")


