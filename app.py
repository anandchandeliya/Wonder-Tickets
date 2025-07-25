from flask import Flask, render_template, request
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book_ticket():
    name = request.form['name']
    event = request.form['event']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bookings (name, event) VALUES (%s, %s)", (name, event))
    conn.commit()
    conn.close()

    return render_template('success.html', name=name, event=event)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
