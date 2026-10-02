SELECT
    product_id,
    product_name,
    category,
    price,
    price_category,
    discount_percentage,
    rating,
    stock,
    stock_status,
    brand,
    sku
FROM {{ ref('int_fakeproducts') }}