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

    print("\nRevenue by Category:")
    print(run_query("queries/revenue_by_category.sql"))

    print("\nRepeat Customers:")
    print(run_query("queries/repeat_customers.sql"))

    print("\nMonthly New Customers:")
    print(run_query("queries/monthly_new_customers.sql"))


if __name__ == "__main__":
    main()
