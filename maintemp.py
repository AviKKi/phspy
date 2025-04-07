import logging
import argparse
import pandas as pd
from utils import (
    generate_date_range,
    ProductHuntClient,
    get_products_on_date,
    get_full_product_info
)

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    
    parser = argparse.ArgumentParser(description = 'Product Hunt Crawler')
    parser.add_argument('--start_date', required = True, help = 'Start date in YYYY-MM-DD format')
    parser.add_argument('--end_date', required = True, help = 'End date in YYYY-MM-DD format')

    args = parser.parse_args()

    logging.debug(f"Starting product crawl from {args.start_date} to {args.end_date}")

    # Generate the list of dates to crawl
    try:
        dates_to_crawl = generate_date_range(args.start_date, args.end_date)
        logging.debug(f"Generated date range: {dates_to_crawl}")
    except Exception as e:
        logging.error(f"Error generating date range: {e}", exc_info=True)
        return

    if not dates_to_crawl:
        logging.error("No valid dates found. Exiting...")
        return

    try:
        client = ProductHuntClient()
        logging.debug("Initialized ProductHuntClient successfully.")
    except Exception as e:
        logging.critical(f"Failed to initialize ProductHuntClient: {e}", exc_info=True)
        return

    all_data = []
    for date in dates_to_crawl:
        try:
            year, month, day = date.split("-")
            logging.info(f"Fetching products for {date}...")

            # Get products for the given date
            products = get_products_on_date(client, int(year), int(month), int(day))
            logging.debug(f"Retrieved products: {products}")

            if not products:
                logging.warning(f"No products found for {date}")
                continue

            for product in products[:40]:
                try:
                    slug = product.get("slug")
                    if not slug:
                        logging.error(f"Missing 'slug' in product data: {product}")
                        continue

                    logging.info(f"Fetching full details for product: {slug}")

                    # Get full product information
                    full_info = get_full_product_info(client, slug)
                    logging.debug(f"Full info retrieved: {full_info}")

                    logging.info(f"Product {slug} details retrieved successfully.")
                    all_data.append({
                        **product,
                        **full_info.get("product_details", {}),
                        **full_info.get("product_about", {})
                        })
                except Exception as e:
                    logging.error(f"Error retrieving details for product {product}: {e}", exc_info=True)
        except Exception as e:
            logging.error(f"Error processing date {date}: {e}", exc_info=True)
    df = pd.DataFrame(all_data)
    df.to_excel("producthunt_output.xlsx", index=False)

if __name__ == "__main__":
    main()
