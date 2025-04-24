from flask import Flask, request, render_template
from flask_cors import CORS  # Import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def db_connect():
    return sqlite3.connect('users.db')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = db_connect()
    cursor = conn.cursor()

    # VULNERABLE QUERY (SQL Injection possible here)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        return render_template('home.html', username=username)
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    app.run(debug=True)
