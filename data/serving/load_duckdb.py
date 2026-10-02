import duckdb

DB_PATH = "data/serving/products.duckdb"


def load_duckdb(products):
    # Connexion à DuckDB
    # Le fichier est créé automatiquement s'il n'existe pas
    con = duckdb.connect(DB_PATH)

    # Création de la table si elle n'existe pas
    con.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_name VARCHAR,
            price_category VARCHAR,
            stock_status VARCHAR
        )
    """)

    # Nettoyage de l'ancienne donnée
    con.execute("DELETE FROM products")

    # Chargement des données transformées
    for product in products:
        con.execute("""
            INSERT INTO products (
                product_name,
                price_category,
                stock_status
            )
            VALUES (?, ?, ?)
        """, (
            product["product_name"],
            product["price_category"],
            product["stock_status"]
        ))

    con.close()

    print(f"✅ {len(products)} produits chargés dans DuckDB")


if __name__ == "__main__":
    print("🚀 Load DuckDB prêt")