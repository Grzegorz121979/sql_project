import sqlite3
from users import User

conn = sqlite3.connect('data.db')

c = conn.cursor()

# c.execute("CREATE TABLE users (user text, password text)")

user_1 = User('Greg', '123')
user_2 = User('Tom', '456')
user_3 = User('Sue', '789')

def create_new_user(class_name, user: str, password: str) -> User | None:
    """
    function to create new instans User class
    """
    return User(user, password)

def insert_new_user(U: User, u: str, p: str) -> None:
    """
    function insert new user to sql table
    """
    with conn:
        c.execute("INSERT INTO users VALUES (:user, :password)", {'user': create_new_user(U, u, p).name, 'password': create_new_user(U, u, p).password})

# c.execute("INSERT INTO users VALUES (:name, :password)", {'name': user_1.name, 'password': user_1.password})
# conn.commit()
#
# c.execute("INSERT INTO users VALUES (:name, :password)", {'name': user_2.name, 'password': user_2.password})
# conn.commit()
#
# c.execute("INSERT INTO users VALUES (:name, :password)", {'name': user_3.name, 'password': user_3.password})
# conn.commit()

user_name = input('Name: ')
password_entry = input('Password: ')
insert_new_user(User, user_name, password_entry)

c.execute("SELECT * FROM users")
print(c.fetchall())

conn.commit()
conn.close()
