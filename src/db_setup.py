import sqlite3

def setup_database(db_path="analytics.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript(open("schema.sql").read())
    conn.commit()
    conn.close()
