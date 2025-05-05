
import pandas as pd
from crawler.utils import parse_args
from crawler.utils import generate_date_range
from crawler.utils import ProductHuntClient, get_products_on_date, get_product_details, get_product_about, get_product_comments
from time import sleep

def main(start_date, end_date):
    date_list = generate_date_range(start_date, end_date)

    if not date_list:
        return pd.DataFrame()  # Return empty DataFrame if no valid dates

    client = ProductHuntClient()
    all_products = []

    for date in date_list:
        year, month, day = map(int, date.split('-'))
        products = get_products_on_date(client, year, month, day)

        if products:
            all_products.extend(products)

    df = pd.DataFrame(all_products)
    slugs = df['slug'].tolist() if 'slug' in df.columns else []

    products_details = []
    for slug in slugs[:10]:
        try:
            print(f"collecting data for {slug}")
            about = get_product_details(client, slug)
            if about:
                products_details.append(about)
                print(f"Collected data for {slug}")

        except Exception as e:
            print(f"Failed to collect data for {slug}: {e}")

    product_details_df = pd.DataFrame(products_details)
    

    products_about = []
    for slug in slugs[:10]:
        try:
            print(f"collecting data for {slug}")
            about = get_product_about(client, slug)
            if about:
                products_about.append(about)
                print(f"Collected data for {slug}")

        except Exception as e:
            print(f"Failed to collect data for {slug}: {e}")
        
    product_about_df = pd.DataFrame(products_about)

    main_descriptive_comments = []
    for slug in slugs[:10]:
        try:
            print(f"collecting data for {slug}")
            comment = get_product_comments(client, slug)
            if comment:
                main_descriptive_comments.extend(comment)
                print(f"collected data for {slug}")
        
        except Exception as e:
            print(f" Failed to collect data for {slug}: {e}")

    main_comments_df = pd.DataFrame(main_descriptive_comments)

    merged_df = df.merge(product_details_df, on='slug', how='outer') \
               .merge(product_about_df, on='slug', how='outer') \
               .merge(main_comments_df, on='slug', how='outer')

    return merged_df


if __name__ == '__main__':
    args = parse_args()
    df = main(args.start_date, args.end_date)
    df.to_csv('products5.csv', index=False)
    # print(df)

