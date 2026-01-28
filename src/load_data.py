import csv
import sqlite3

def load_sales_data(csv_path, db_path="analytics.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(csv_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT INTO sales
                (order_id, customer_id, product, category, order_date, quantity, price)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                row["order_id"],
                row["customer_id"],
                row["product"],
                row["category"],
                row["order_date"],
                row["quantity"],
                row["price"]
            ))

    conn.commit()
    conn.close()
