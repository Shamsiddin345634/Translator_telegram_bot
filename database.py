import sqlite3

class Translate():
    def __init__(self):
        self.connection = sqlite3.connect('tarjima.db')
        self.cursor = self.connection.cursor()
    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id integer,
            first_name varchar(65),
            user_name varchar(65)
        )""")
    def add_user(self,user_id,firstname, username):
        self.cursor.execute("INSERT INTO users VALUES ({},'{}','{}')".format(user_id, firstname, username))
        self.connection.commit()
    def user_exist(self, userid):
        self.cursor.execute(f"SELECT user_id FROM users WHERE user_id = {userid}")
        data = self.cursor.fetchone()
        return data