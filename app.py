from flask import Flask
import mysql.connector
import os
import time

app = Flask(__name__)

def get_db_connection():
    # Retry logic to wait for MySQL to be ready
    retries = 5
    while retries > 0:
        try:
            return mysql.connector.connect(
                host=os.getenv('DB_HOST', 'db'),
                user=os.getenv('DB_USER', 'user'),
                password=os.getenv('DB_PASSWORD', 'password'),
                database=os.getenv('DB_NAME', 'appdb')
            )
        except mysql.connector.Error:
            retries -= 1
            time.sleep(5)
    return None

@app.route('/')
def index():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"<h1>Success!</h1><p>Connected to MySQL version: {version[0]}</p>"
    return "<h1>Error</h1><p>Could not connect to the database.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
