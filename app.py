import os
from flask import Flask, request, render_template, jsonify
from scraper import scrape_example
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
conn = sqlite3.connect('scraped_data.db')
conn.execute('''CREATE TABLE IF NOT EXISTS products
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT NOT NULL,
                 price TEXT NOT NULL)''')
conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    data = scrape_example(url)
    if 'error' in data:
        return jsonify(data), 500  # Return 500 Internal Server Error if there's an error
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)
