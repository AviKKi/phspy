from crawler.utils import ProductHuntClient, get_product_details, get_product_comments

# Replace with the actual slug you want to test
slug = 'readdy'

client = ProductHuntClient()

# Run get_product_details
details = get_product_details(client, slug)
print("Product Details:")
print(details)

# # Run get_product_comments
# comments = get_product_comments(client, slug)
# print("\nProduct Comments:")
# print(comments)

# If you have another function like get_product_about, run it similarly:
# about = get_product_about(client, slug)
# print("\nProduct About:")
# print(about)
