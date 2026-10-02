from typing import Any


REQUIRED_PRODUCT_FIELDS = {
    "id": int,
    "title": str,
    "description": str,
    "category": str,
    "price": (int, float),
    "discountPercentage": (int, float),
    "rating": (int, float),
    "stock": int,
    "tags": list,
    "sku": str,
    "weight": (int, float),
    "dimensions": dict,
    "warrantyInformation": str,
    "shippingInformation": str,
    "availabilityStatus": str,
    "reviews": list,
    "returnPolicy": str,
    "minimumOrderQuantity": int,
    "meta": dict,
    "images": list,
    "thumbnail": str,
}


DIMENSION_FIELDS = {
    "width": (int, float),
    "height": (int, float),
    "depth": (int, float),
}


META_FIELDS = {
    "createdAt": str,
    "updatedAt": str,
    "barcode": str,
    "qrCode": str,
}


REVIEW_FIELDS = {
    "rating": int,
    "comment": str,
    "date": str,
    "reviewerName": str,
    "reviewerEmail": str,
}


def validate_field_types(data: dict, schema: dict, context: str):
    errors = []

    for field, expected_type in schema.items():

        if field not in data:
            errors.append(f"{context}: missing field '{field}'")
            continue

        value = data[field]

        # brand can be nullable / optional
        if value is None:
            continue

        if not isinstance(value, expected_type):
            errors.append(
                f"{context}: '{field}' expected "
                f"{expected_type}, got {type(value).__name__}"
            )

    return errors


def validate_product(product: dict, index: int):
    errors = []

    context = f"products[{index}]"

    # Main product fields
    errors.extend(
        validate_field_types(
            product,
            REQUIRED_PRODUCT_FIELDS,
            context
        )
    )

    # Brand is nullable
    if "brand" in product and product["brand"] is not None:
        if not isinstance(product["brand"], str):
            errors.append(
                f"{context}: 'brand' must be string or null"
            )

    # Dimensions
    if isinstance(product.get("dimensions"), dict):
        errors.extend(
            validate_field_types(
                product["dimensions"],
                DIMENSION_FIELDS,
                f"{context}.dimensions"
            )
        )

    # Meta
    if isinstance(product.get("meta"), dict):
        errors.extend(
            validate_field_types(
                product["meta"],
                META_FIELDS,
                f"{context}.meta"
            )
        )

    # Tags
    if isinstance(product.get("tags"), list):
        for i, tag in enumerate(product["tags"]):
            if not isinstance(tag, str):
                errors.append(
                    f"{context}.tags[{i}] must be string"
                )

    # Images
    if isinstance(product.get("images"), list):
        for i, image in enumerate(product["images"]):
            if not isinstance(image, str):
                errors.append(
                    f"{context}.images[{i}] must be string"
                )

    # Reviews
    if isinstance(product.get("reviews"), list):
        for i, review in enumerate(product["reviews"]):

            if not isinstance(review, dict):
                errors.append(
                    f"{context}.reviews[{i}] must be object"
                )
                continue

            errors.extend(
                validate_field_types(
                    review,
                    REVIEW_FIELDS,
                    f"{context}.reviews[{i}]"
                )
            )

    return errors


def validate_products_response(data: dict):
    errors = []

    # Root validation
    if not isinstance(data, dict):
        return ["Response must be a JSON object"]

    # Root fields
    if "products" not in data:
        errors.append("Missing root field 'products'")
    elif not isinstance(data["products"], list):
        errors.append("'products' must be an array")

    if "total" not in data:
        errors.append("Missing root field 'total'")
    elif not isinstance(data["total"], int):
        errors.append("'total' must be integer")

    if "skip" not in data:
        errors.append("Missing root field 'skip'")
    elif not isinstance(data["skip"], int):
        errors.append("'skip' must be integer")

    if "limit" not in data:
        errors.append("Missing root field 'limit'")
    elif not isinstance(data["limit"], int):
        errors.append("'limit' must be integer")

    # Product validation
    if isinstance(data.get("products"), list):

        for index, product in enumerate(data["products"]):
            if not isinstance(product, dict):
                errors.append(
                    f"products[{index}] must be object"
                )
                continue

            errors.extend(
                validate_product(product, index)
            )

    return errors