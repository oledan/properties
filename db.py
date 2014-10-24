import MySQLdb

conn = MySQLdb.connect (
  host = "localhost",
  user = "root",
  passwd = "password",
  db = "properties",
  port = 8000)

cursor = conn.cursor()

#Database Functions
def display(aCursor):
  rows = cursor.fetchall()
  for r in rows:
    print r

def get_from_db(query):
  cursor.execute(query)
  rows = []
  for row in cursor:
    rows.append(row)
  return rows

def add_to_db(query):
  cursor.execute(query)
  return "added to db"

def fetchone(query):
  cursor.fetchone(query)
  return display(cursor)
