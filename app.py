from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Issue 1: Hardcoded database path
DB_PATH = "users.db"

@app.route("/user")
def get_user():
    user_id = request.args.get("id")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Issue 2: SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)

    result = cursor.fetchone()
    conn.close()

    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
  
