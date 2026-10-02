def remove_duplicates(products):
    seen_ids = set()
    clean_products = []

    for product in products:
        product_id = product.get("id")

        if product_id in seen_ids:
            continue

        seen_ids.add(product_id)
        clean_products.append(product)

    return clean_products