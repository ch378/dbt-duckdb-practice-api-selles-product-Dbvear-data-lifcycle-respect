from faker import Faker
import pandas as pd
import random

fake = Faker()

products = []

categories = [
    "smartphones",
    "laptops",
    "tablets",
    "accessories",
    "audio"
]

for product_id in range(1, 1001):

    product = {
        "id": product_id,
        "product_name": fake.catch_phrase(),
        "description": fake.text(max_nb_chars=150),
        "category": random.choice(categories),
        "price": round(random.uniform(10, 1000), 2),
        "discount_percentage": round(random.uniform(0, 30), 2),
        "rating": round(random.uniform(1, 5), 2),
        "stock": random.randint(0, 100),
        "brand": fake.company(),
        "sku": f"SKU-{product_id:05d}",
        "weight": round(random.uniform(0.1, 10), 2),
        "warranty_information": "1 year warranty",
        "shipping_information": "Ships in 3-5 business days",
        "availability_status": "In Stock",
        "return_policy": "30 days",
        "minimum_order_quantity": random.randint(1, 10)
    }

    products.append(product)

df = pd.DataFrame(products)

df.to_csv(
    "data/serving/products.csv",
    index=False
)

print(f"{len(df)} products generated")
print("CSV: data/serving/products.csv")