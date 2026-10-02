from data.ingestion.fetch_products import fetch_all_products
from data.transformation.validation import validate_products_response
from data.transformation.Cleaning import remove_duplicates
from data.transformation.transformation import transform_products
from data.serving.load_duckdb import load_duckdb


def main():

    print("🚀 Pipeline started")

    # Ingestion
    data = fetch_all_products()

    # Validation
    errors = validate_products_response(data)

    if errors:
        print("❌ Validation failed")
        for error in errors:
            print("-", error)
        return

    print("✅ Validation passed")

    products = data["products"]

    # Cleaning
    products = remove_duplicates(products)

    # Transformation
    products = transform_products(products)

    # Serving
    load_duckdb(products)

    print("✅ Pipeline completed")


if __name__ == "__main__":
    main()