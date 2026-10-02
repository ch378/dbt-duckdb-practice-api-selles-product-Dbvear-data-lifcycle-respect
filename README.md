# dbt-duckdb-practice-api-selles-product-Dbvear-data-lifcycle-respect
# DBT DuckDB Practice — Product Data Engineering

A practical **Data Engineering** project demonstrating an end-to-end data lifecycle using **Python, Faker, DuckDB and dbt Core**.

The project covers data ingestion, transformation, data quality, data modeling, documentation and lineage.

## Project Overview

```text
api/CSV / Generated Data
        |
        v
     Ingestion
        |
        v
      DuckDB
        |
        v
   dbt Staging
        |
        v
 dbt Intermediate
        |
        v
    dbt Marts
```

## Tech Stack
* **api=https://dummyjson.com/products**
* **Python** — Data generation and ingestion
* **Faker** — Synthetic product data
* **Pandas** — Data manipulation
* **DuckDB** — Analytical database
* **dbt Core** — Data transformation and testing
* **SQL** — Data modeling
* **DBeaver** — Database exploration
* **Git / GitHub** — Version control

## Project Structure

```text
my_project/
│
├── dbt_project.yml
├── README.md
├── .gitignore
│
├── seeds/
│   └── fakeproducts.csv
│
├── models/
│   ├── schema.yml
│   │
│   ├── staging/
│   │   └── stg_fakeproducts.sql
│   │
│   ├── intermediate/
│   │   └── int_fakeproducts.sql
│   │
│   └── marts/
│       ├── mart_products.sql
│       └── mart_out_of_stock.sql
│
└── tests/
```

## Data Lifecycle

```text
api/fakeproducts.csv
       |
       | dbt seed
       v
   fakeproducts
       |
       v
stg_fakeproducts
       |
       v
int_fakeproducts
       |
       +----------------------+
       |                      |
       v                      v
mart_products        mart_out_of_stock
```

## Dataset

The project uses a synthetic product dataset containing:

```text
id
product_name
description
category
price
discount_percentage
rating
stock
brand
sku
weight
warranty_information
shipping_information
availability_status
return_policy
minimum_order_quantity
```

## Data Transformations

### Price Category

```text
price < 50        → Low
50 <= price <= 200 → Medium
price > 200       → High
```

### Stock Status

```text
stock = 0          → Out of Stock
1 <= stock <= 10   → Low Stock
stock > 10         → In Stock
```

## Data Quality

dbt tests are defined in `models/schema.yml`.

Examples:

```text
not_null
unique
accepted_values
```

Example:

```yaml
- name: product_id
  data_tests:
    - not_null
    - unique
```

## Installation

Create and activate a Python virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dbt:

```powershell
pip install dbt-core dbt-duckdb
```

Verify installation:

```powershell
dbt --version
```

## Run the Project

Load the CSV into DuckDB:

```powershell
dbt seed
```

Validate the project:

```powershell
dbt parse
```

Run dbt models:

```powershell
dbt run
```

Run models and tests together:

```powershell
dbt build
```

Run data quality tests:

```powershell
dbt test
```

## Documentation & Lineage

Generate dbt documentation:

```powershell
dbt docs generate
```

Start the documentation server:

```powershell
dbt docs serve
```

The dbt documentation provides:

* Model documentation
* Column information
* Data tests
* Dependencies
* Data lineage

## DuckDB

The project uses a single DuckDB database:

```text
products.duckdb
│
└── main
    ├── fakeproducts
    ├── stg_fakeproducts
    ├── int_fakeproducts
    ├── mart_products
    └── mart_out_of_stock
```



## Author**Hamza Chadli**
**data lineage**
<img width="1920" height="1106" alt="Screenshot 2026-10-02 111635" src="https://github.com/user-attachments/assets/fcbcdb56-a1ef-450d-af06-7c86837547da" />
**db shema**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/aca2727d-f4e8-42e5-b334-c9f39f92ee21" />

