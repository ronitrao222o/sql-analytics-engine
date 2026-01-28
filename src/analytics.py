import sqlite3

def run_query(query_file, db_path="analytics.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = open(query_file).read()
    cursor.execute(query)

    results = cursor.fetchall()
    conn.close()
    return results
