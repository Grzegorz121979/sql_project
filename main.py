import sqlite3
from users import User

conn = sqlite3.connect('data.db')

c = conn.cursor()

c.execute("CREATE TABLE users (user text, password text)")
