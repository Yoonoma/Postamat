import os.path
from resources.config import PWD_DB
import sqlite3

from loguru import logger

### Shell SQLite
# class SQLite():
#     def __init__(self, file):
#         self.file=file
#     def __enter__(self):
#         self.conn = sqlite3.connect(self.file)
#         self.conn.row_factory = sqlite3.Row
#         return self.conn.cursor()
#     def __exit__(self, type, value, traceback):
#         self.conn.commit()
#         self.conn.close()

## Функция проверяет наличие БД и создает ее в случае необходимости

def check_db():
    check_file_db = os.path.exists(PWD_DB)
    if not check_file_db:
        # Log
        logger.error("Database not found!")

        # creating tables
        try:
            logger.warning("Database creation...")

            connect_sql = sqlite3.connect(PWD_DB)
            cursor_db = connect_sql.cursor()

            # sqlite_create_table_cells_query = """
            #     CREATE TABLE Cells (
            #     id integer PRIMARY KEY AUTOINCREMENT,
            #     is_taken_tag boolean NOT NULL DEFAULT 0,
            #     is_close boolean NOT NULL DEFAULT 1,
            #     Tags_id integer NOT NULL,
            #     CONSTRAINT Cells_Tags FOREIGN KEY (Tags_id)
            #     REFERENCES Tags (id)
            # );
            # """
            #
            # sqlite_create_table_staff_query = """
            #     CREATE TABLE Staff (
            #     id integer PRIMARY KEY AUTOINCREMENT,
            #     "key" integer NOT NULL,
            #     is_taken_tag boolean NOT NULL DEFAULT 0,
            #     Tags_id integer NOT NULL,
            #     CONSTRAINT Users_Tags FOREIGN KEY (Tags_id)
            #     REFERENCES Tags (id)
            # );
            # """

            # sqlite_create_table_tags_query = """
            # CREATE TABLE Tags (
            #     id integer PRIMARY KEY AUTOINCREMENT,
            #     battery_charge integer DEFAULT 100
            # );
            #  """
            #
            # sqlite_create_table_keys_query = """
            # CREATE TABLE Keys (
            #     id INTEGER PRIMARY KEY AUTOINCREMENT,
            #     key_RFID integer,
            #     key_QR integer,
            #     FOREIGN KEY (id)  REFERENCES Tags (Tag_id)
            # );
            # """

            # cursor_db.execute(sqlite_create_table_cells_query)
            # cursor_db.execute(sqlite_create_table_staff_query)
            # cursor_db.execute(sqlite_create_table_tags_query)
            # cursor_db.execute(sqlite_create_table_keys_query)

            query_create_table_user = """
            CREATE TABLE User (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_tag INTEGER DEFAULT 0,   
                key_tag VARCHAR(50),
                id_RFID VARCHAR(50),
                id_QR VARCHAR(50),
                is_taked NUMBER(1) DEFAULT 0
            );  
            """

            cursor_db.execute(query_create_table_user)

            connect_sql.commit()
            connect_sql.close()
            logger.debug("Database created.")
        except sqlite3.Error as er:
            logger.error("Failed to create database : ", er)

    check_file_db = os.path.exists(PWD_DB)

    # Log
    if check_file_db:
        logger.info("Database is ready to go.")
    else:
        logger.error("Failed to create database!")
    return check_file_db

