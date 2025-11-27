import psycopg2
from typing import Optional
from utils import settings


conn = psycopg2.connect(
    host = "127.0.0.1",
    port = "5432",
    database = "fastapi_app_db",
    user = "diana1215",
    password = settings.DB_PASSWORD
)


curs = conn.cursor()


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
                
    # if columns is not None:
    #     for column in columns:
    #         cursor.execute(query, (table, column))
            
    #         rows = cursor.fetchall()
    #         for row in rows:
    #             if row is None:
    #                 return False
    #             else:
    #                 return True





def add_data_to_db(cursor, arr: dict):
    data = check_if_columm_in_table(cursor=cursor, table="users", column=None, arr=arr)
    if data is False:
        return 'я твою мать ебал'
    else:
        return 'щй иди нахуй'

print(add_data_to_db(cursor=curs, arr=user_data))
















# smth = "email"

# query = """SELECT column_name
#     FROM information_schema.columns
#     WHERE table_schema = 'public'
#      AND table_name = 'users' 
#      AND column_name = %s;"""



# curs.execute(query, (smth,))

# # records = curs.fetchall()
# rows = curs.fetchall()
# for row in rows:
#     print(row)