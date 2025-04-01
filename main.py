import argparse
from utils import generate_date_range
from utils import ProductHuntClient, get_products_on_date

def main():
    parser = argparse.ArgumentParser(description = 'Product Hunt Crawler')
    parser.add_argument('--start_date', required = True, help = 'Start date in YYYY-MM-DD format')
    parser.add_argument('--end_date', required = True, help = 'End date in YYYY-MM-DD format')

    args = parser.parse_args()

    date_list = generate_date_range(args.start_date, args.end_date)

    if not date_list:
        print(f'No valid dates to crawl.')
        return
    
    print(f'Dates to crawl: {date_list}\n')

    client = ProductHuntClient()

    for date in date_list:
        year, month, day = map(int, date.split('-'))
        print(f'Fetching products for {date}...\n')

        products = get_products_on_date(client, year, month, day)

        if products:
            print(f'Total products retrieved for {date}: {len(products)}\n')
            for product in products:
                print(f"Name: {product['name']}")
                print(f"Tagline: {product['tagline']}")
                print(f"Votes: {product['votes']}")
                print(f"Launch Date: {product['launch_date']}")
                print(f"Topics: {product['topics']}")
                print(f"Product URL: {product['product_url']}")
                print('-' * 50)
            print(f'Total products retrieved for {date}: {len(products)}\n')
        else:
            print(f'No products found for {date}.\n')

            

if __name__ == '__main__':
    main()

