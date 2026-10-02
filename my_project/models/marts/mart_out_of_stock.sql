SELECT
    product_id,
    product_name,
    category,
    price,
    brand,
    sku
FROM {{ ref('int_fakeproducts') }}
WHERE stock_status = 'Out of Stock'