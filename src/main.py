from db_setup import setup_database
from load_data import load_sales_data
from analytics import run_query

def main():
    setup_database()
    load_sales_data("data/sales_data.csv")

    print("Top Customers:")
    print(run_query("queries/top_customers.sql"))

    print("\nMonthly Revenue:")
    print(run_query("queries/monthly_revenue.sql"))

if __name__ == "__main__":
    main()
