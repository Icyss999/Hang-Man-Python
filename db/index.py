import sqlite3;



DB_FILE_PATH = "./table/database.db"


def get_db():
    # So basically we create a database instance 
     db = sqlite3.connect(DB_FILE_PATH)
    # We set its way of accessing the table via row    
     db.row_factory = sqlite3.Row
     return db




