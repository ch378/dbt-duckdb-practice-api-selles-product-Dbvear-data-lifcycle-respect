SELECT
    product_name,
    price_category,
    stock_status
FROM {{ ref('stg_products') }}
WHERE stock_status = 'Low Stock'