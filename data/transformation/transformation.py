def transform_product(product):
    price = product["price"]
    stock = product["stock"]

    # Price category
    if price < 50:
        price_category = "Low"
    elif price <= 200:
        price_category = "Medium"
    else:
        price_category = "High"

    # Stock status
    if stock == 0:
        stock_status = "Out of Stock"
    elif stock <= 10:
        stock_status = "Low Stock"
    else:
        stock_status = "In Stock"

    return {
        "product_name": product["title"],
        "price_category": price_category,
        "stock_status": stock_status
    }


def transform_products(products):
    return [transform_product(product) for product in products]