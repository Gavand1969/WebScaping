import requests
from bs4 import BeautifulSoup
import sqlite3

def scrape_example(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        products = []
        for product in soup.select('.product'):
            title = product.select_one('.title').text
            price = product.select_one('.price').text
            products.append([title, price])

        # Save to SQLite database
        try:
            conn = sqlite3.connect('scraped_data.db')
            cur = conn.cursor()
            for product in products:
                cur.execute("INSERT INTO products (title, price) VALUES (?, ?)", product)
            conn.commit()
        except sqlite3.Error as e:
            return {'error': f"Error saving data to database: {e}"}
        finally:
            conn.close()

        return products
    except requests.exceptions.RequestException as e:
        return {'error': f"Error fetching data from URL: {e}"}
    except Exception as e:
        return {'error': f"An unexpected error occurred: {e}"}

