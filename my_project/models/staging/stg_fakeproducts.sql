SELECT
    id AS product_id,
    product_name,
    description,
    category,
    price,
    discount_percentage,
    rating,
    stock,
    brand,
    sku,
    weight,
    warranty_information,
    shipping_information,
    availability_status,
    return_policy,
    minimum_order_quantity
FROM {{ ref('fakeproducts') }}