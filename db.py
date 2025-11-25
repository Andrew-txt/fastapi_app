import psycopg2

from utils import settings


conn = psycopg2.connect(
    host = "127.0.0.1",
    port = "5432",
    database = "fastapi_app_db",
    user = "diana1215",
    password = settings.DB_PASSWORD
)

query = """SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name = 'users' 
  AND column_name = 'smth'"""

curs = conn.cursor()
curs.execute(query)

# SELECT column_name
# FROM information_schema.columns
# WHERE table_schema = 'public'
#   AND table_name = 'users' 
#   AND column_name = 'name';


rows = curs.fetchall()
for row in rows:
    print(row)