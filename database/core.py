import sqlite3
import sys
from random import randint

from loguru import logger
from resources.config import TablesDatabase, database


class SQLiteDB:
    def __init__(self, db_file_path: str):
        self.REQUEST_FAILED = -1  # ошибка запроса
        self.tables = TablesDatabase

        try:
            # Подключения к БД
            self.sqliteConnection = sqlite3.connect(db_file_path,
                                                    check_same_thread=False)  # отключаем проверки на потоки
            # Создание курсора базы данных
            self.cursor = self.sqliteConnection.cursor()
            logger.debug("Database is connected.")

        except sqlite3.Error as error:
            logger.error(f"Database Error : {error}")
            sys.exit(1)

        self.column_names_table_user = self.get_column_names("User")

    # Проверяет rfid-код в БД
    def key_verification(self, id_type_scanner: str, key: str) -> bool:
        sqlite_query = f'SELECT Count({id_type_scanner}) FROM {self.tables.user.value} WHERE {id_type_scanner}="{key}";'
        return self.query(sqlite_query)[0][0]

    # Проверяет статус метки (в наличии/изъята)
    def is_taken_tag(self, id_type_scanner: str, data: str) -> bool:
        sqlite_query = f'SELECT is_taked FROM {self.tables.user.value} WHERE {id_type_scanner}="{data}"'
        return self.query(sqlite_query)[0][0]

    # Сотрудник взял метку
    def taken_tag(self, id_type_scanner: str, data: str):
        sqlite_query = f'UPDATE {self.tables.user.value} SET is_taked=1 WHERE {id_type_scanner}="{data}";'
        self.cursor.execute(sqlite_query)
        self.sqliteConnection.commit()

    # Сотрудник вернул метку в шкаф
    def returned_tag(self, id_type_scanner: str, data):
        sqlite_query = f'UPDATE {self.tables.user.value} SET is_taked=0 WHERE {id_type_scanner}="{data}";'
        self.cursor.execute(sqlite_query)
        self.sqliteConnection.commit()

    # Возвращет имена столбоц таблицы
    def get_column_names(self, name_table: str) -> list:
        sqlite_query = f'PRAGMA table_info("{name_table}");'
        result = self.query(sqlite_query)
        column_names = [i[1] for i in result]
        return column_names

    # Возвращает список список таблицы
    def get_data_table(self, name_table: str) -> list:
        sqlite_query = f"SELECT * FROM {name_table}"
        return self.query(sqlite_query)

    # Возвращает количество записей в таблице
    def get_count_row(self, name_table: str) -> int:
        sqlite_query = f"SELECT COUNT(*) FROM {name_table};"
        return self.query(sqlite_query)[0][0]

    # Возвращает количество столбцов в таблице
    def get_count_column(self, name_table: str) -> int:
        return len(self.get_column_names(name_table))

    # Возвращает запись из таблицы
    def get_record(self, name_table: str, row_number: int, column_list='*') -> tuple:
        sqlite_query = f"SELECT {column_list} FROM {name_table} WHERE id={row_number};"
        result = self.cursor.execute(sqlite_query).fetchall()[0]
        return result

    # Удаляет запись из таблицы по первичному ключу
    def delete_primary_key_record(self, name_table: str, row_number: int) -> None:
        sqlite_query = f"DELETE FROM {name_table} WHERE id={row_number}"
        self.cursor.execute(sqlite_query)
        self.sqliteConnection.commit()

    # Удаляет запись из таблицы по условию
    def delete_record_where(self, name_table: str, condition="AND", **where):
        sqlite_where = f" {condition} ".join([f'"{name_column}"="{value}"' for name_column, value in where.items()])
        sqlite_query = f'DELETE FROM {name_table} WHERE {sqlite_where} LIMIT 1;'
        self.cursor.execute(sqlite_query)
        self.sqliteConnection.commit()

    # Создает нового пользователя
    def new_user(self, key_qr, key_rfid):
        qr_key = database["QR_PREFIX"] + str(randint(1000, 99999))
        id_tag = self.get_count_row(self.tables.user.value) + 1
        sqlite_query = f'INSERT INTO User (id_tag, key_tag, id_rfid, id_QR) VALUES("{id_tag}", "{key_qr}", "{key_rfid}", "{qr_key}");'
        self.cursor.execute(sqlite_query)
        self.sqliteConnection.commit()

    def get_id_tag(self, id_type_scanner: str, key_scanner: str) -> int:
        sqlite_query = f'SELECT id_tag FROM {self.tables.user.value} WHERE {id_type_scanner}="{key_scanner}"'
        return int(self.cursor.execute(sqlite_query).fetchone()[0])

    def query(self, sql_query: str):
        result = self.cursor.execute(sql_query).fetchall()
        if result is None:
            logger.warning(f"Request error : [{sql_query}]")
            return self.REQUEST_FAILED
        return result

    # Сохранение изменений и закрытие базы данных
    def close(self):
        self.sqliteConnection.commit()
        self.sqliteConnection.close()
