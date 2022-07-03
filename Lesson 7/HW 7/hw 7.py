import sqlite3
from typing import List, Dict

from flask import Flask, render_template
import json

app = Flask('Mysite')


def db_cursor():
    with sqlite3.connect('purchases.sqlite3') as db_connection:
        db_connection.row_factory = sqlite3.Row
        cursor = db_connection.cursor()
        return cursor


@app.route('/')
def all_purchases():
    """Показати всі покупки"""
    cursor = db_cursor()
    purchases_cursor = cursor.execute("""
            SELECT naming, category, amount, price, customer 
            FROM purchases
        """)
    purchases = [dict(i) for i in purchases_cursor]
    return render_template('purchases.html', result=purchases, enumerate=enumerate)


@app.route('/category/<string:word>/')
def by_category(word: str):
    """Показати всі покупки конкретної категорії (категорія передається через URL)"""
    cursor = db_cursor()
    sql_request = """
        SELECT naming, category, amount, price, customer 
        FROM purchases 
        WHERE category=(?)    
    """
    purchases_cursor = cursor.execute(sql_request, (word,))
    purchases = [dict(i) for i in purchases_cursor]
    return render_template('purchases.html', result=purchases, enumerate=enumerate)


@app.route('/customer/<string:word>/')
def by_customer(word: str):
    """Показати всі покупки конкретного користувачаї (користувач передається через URL)"""
    cursor = db_cursor()
    sql_request = """
            SELECT naming, category, amount, price, customer 
            FROM purchases 
            WHERE customer=(?)    
        """
    purchases_cursor = cursor.execute(sql_request, (word,))
    purchases = [dict(item) for item in purchases_cursor]
    return render_template('purchases.html', result=purchases, enumerate=enumerate)


@app.route('/naming/<string:first_symbols>/')
def by_naming(first_symbols: str):
    """Для пошуку в базі даних використовуйте sql конструкції where та like"""
    cursor = db_cursor()
    first_symbols += '%'
    sql_request = """
            SELECT naming, category, amount, price, customer 
            FROM purchases 
            WHERE naming LIKE (?)    
                  """
    purchases_cursor = cursor.execute(sql_request, (first_symbols,))
    purchases = [dict(item) for item in purchases_cursor]
    print(purchases)
    return render_template('purchases.html', result=purchases, enumerate=enumerate)


if __name__ == '__main__':
    app.run()
