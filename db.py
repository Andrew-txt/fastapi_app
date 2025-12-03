import psycopg2
from typing import Optional
import os
import jwt
from psycopg2 import sql



conn = psycopg2.connect(
    host = "127.0.0.1",
    port = "5432",
    database = "fastapi_app_db",
    user = "diana1215",
    password = os.getenv("DB_PASSWORD")
)

curs = conn.cursor()


# функция проверит есть ли стобец в нужной таблицу в дб, получив их на прямую или через словарь/ тестила
def check_if_columm_in_table(cursor, table, column: Optional[str], arr: Optional[dict]):  #, columns: Optional[list]
    query = """SELECT column_name
        FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = %s 
          AND column_name = %s;"""
    
    if column is not None:
        cursor.execute(query, (table, column))
        row = cursor.fetchone()
        if row is None:
            return False
        else:
            return True

    if arr is not None:
        for key in arr:
            cursor.execute(query, (table, key))

            rows = cursor.fetchall()
            for row in rows:
                if row is None:
                    return False
                else:
                    return True


# получит значения ключей вход словаря и добавит значения в соотвествующие ключам столбцы в дб/ тестила
def add_user_data_to_db(connection, arr: dict):
    try:
        cursor = connection.cursor()
    
        data = check_if_columm_in_table(cursor=cursor, table="users", column=None, arr=arr)
        if data is False:
            return "Column Does Not Exists"
        else:
            columns = ", ".join(arr.keys())
            placeholders = ", ".join(["%s"] * len(arr))
            values = list(arr.values())
        
            query = "INSERT INTO users (%s) VALUES (%s)" % (columns, placeholders)
       
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        
        return "Data Inserted"
    except Exception as e:
        return f"{e}"
    finally:
        if cursor:
            cursor.close()
  




    


