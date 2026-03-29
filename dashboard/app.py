from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("alerts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alerts")
    data = cursor.fetchall()
    return str(data)

if __name__ == "__main__":
    app.run(debug=True)