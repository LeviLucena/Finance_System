import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE_DIR, 'database', 'finance.db')

print("Tentando abrir banco:", DB)
print("Existe o arquivo?", os.path.exists(DB))
print("Existe a pasta?", os.path.exists(os.path.dirname(DB)))

if not os.path.exists(os.path.dirname(DB)):
    os.makedirs(os.path.dirname(DB))

conn = sqlite3.connect(DB)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tabelas no banco:", [t[0] for t in tables])

print("Tabelas no banco:")
for table in tables:
    print(table[0])

conn.close()
