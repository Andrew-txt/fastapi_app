import psycopg2

from utils import settings


conn = psycopg2.connect(
    host = "127.0.0.1",
    port = "5432",
    database = "fastapi_app_db",
    user = "diana1215",
    password = settings.DB_PASSWORD
)

curs = conn.cursor()
curs.execute("SELECT * FROM users")




# rows = curs.fetchall()
# for row in rows:
#     print(row)