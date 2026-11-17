# import sqlite3;
#
#
#
# DB_FILE_PATH = "./table/database.db"
#
#
# def get_db():
#     # So basically we create a database instance
#      db = sqlite3.connect(DB_FILE_PATH)
#     # We set its way of accessing the table via row
#      db.row_factory = sqlite3.Row
#      return db
#
#
#
#
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE_PATH = os.path.join(BASE_DIR, "..", "table", "database.db")


def get_db():
    os.makedirs(os.path.dirname(DB_FILE_PATH), exist_ok=True)
    db = sqlite3.connect(DB_FILE_PATH)
    db.row_factory = sqlite3.Row

    db.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)
    db.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id TEXT PRIMARY KEY,
        user_id TEXT NOT NULL,
        timer INTEGER NOT NULL,
        score INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)
    db.commit()
    return db