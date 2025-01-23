import psycopg2
import os

def main():
    try:
        conn = psycopg2.connect(
            dbname="mydatabase",
            user="user",
            password="password",
            host="172.16.1.2",
            port="5432"
        )
        print("Connected to PostgreSQL successfully!")
        # Выполняем простой запрос
        with conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            print("PostgreSQL version:", version[0])
        conn.close()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

