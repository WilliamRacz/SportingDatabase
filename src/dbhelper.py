# DBHelper.py

import psycopg2
import sys

def connect_db(db_name, user, password, host="localhost", port="5432"):
    """
    Open a connection to PostgreSQL and return the connection object.
    Kill the script on failure (brute-force simple).
    """
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("PostgreSQL connection established.")
        return conn

    except psycopg2.Error as e:
        print(f"[DB ERROR] {e}")
        sys.exit(1)



if __name__ == "__main__":
    conn = connect_db("postgres", "natwat", "")
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    print("Test query result:", cur.fetchone())
    cur.close()
    conn.close()
