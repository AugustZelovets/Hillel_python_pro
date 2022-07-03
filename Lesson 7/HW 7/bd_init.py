import json
import sqlite3

with sqlite3.connect('purchases.sqlite3') as db_connection:
    cursor = db_connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS purchases(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            naming VARCHAR(255) NOT NULL,
            category VARCHAR(50) NOT NULL,
            amount INTEGER NOT NULL,
            price REAL NOT NULL,
            customer VARCHAR(50) NOT NULL
        )
    """)

    cursor.execute("""
       INSERT INTO 
           purchases(naming, category, amount, price, customer) 
       VALUES 
           ("Samsung s10", "smartphone", 1, 500, "Girgio"),
           ("Starfire 235/70R16", "automobile tires", 4, 200, "Helga"),
           ("Cuisinart 14-Inch Stir-Fry Pan", "cookware", 1, 45, "Gustaf"),
           ("Spoons set", "cookware", 1, 15, "Gustaf");
            """)

