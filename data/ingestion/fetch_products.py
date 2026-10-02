from .api_client import get


BASE_URL = "https://dummyjson.com/products"


# 1. Get all products
def fetch_all_products():
    return get(BASE_URL)


# 2. Get a single product
def fetch_product(product_id):
    return get(f"{BASE_URL}/{product_id}")


# 3. Search products
def search_products(query):
    return get(f"{BASE_URL}/search?q={query}")


# 4. Get products with pagination
def fetch_products_paginated(limit=10, skip=0):
    return get(f"{BASE_URL}?limit={limit}&skip={skip}")


# 5. Get products with selected fields
def fetch_products_select(fields):
    select = ",".join(fields)
    return get(f"{BASE_URL}?select={select}")


# 6. Sort products
def fetch_products_sorted(sort_by="title", order="asc"):
    return get(f"{BASE_URL}?sortBy={sort_by}&order={order}")


# 7. Filter by modification date
def fetch_products_modified(modified_after=None, modified_before=None):
    params = []

    if modified_after:
        params.append(f"modifiedAfter={modified_after}")

    if modified_before:
        params.append(f"modifiedBefore={modified_before}")

    url = BASE_URL

    if params:
        url += "?" + "&".join(params)

    return get(url)


# 8. Get all categories
def fetch_categories():
    return get(f"{BASE_URL}/categories")


# 9. Get category list
def fetch_category_list():
    return get(f"{BASE_URL}/category-list")


# 10. Get products by category
def fetch_products_by_category(category):
    return get(f"{BASE_URL}/category/{category}")