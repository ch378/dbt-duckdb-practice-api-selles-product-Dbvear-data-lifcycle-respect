SELECT
    product_id,
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
    minimum_order_quantity,

    CASE
        WHEN price < 50 THEN 'Low'
        WHEN price <= 200 THEN 'Medium'
        ELSE 'High'
    END AS price_category,

    CASE
        WHEN stock = 0 THEN 'Out of Stock'
        WHEN stock <= 10 THEN 'Low Stock'
        ELSE 'In Stock'
    END AS stock_status

FROM {{ ref('stg_fakeproducts') }}