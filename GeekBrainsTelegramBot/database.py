import sqlite3


class User:
    def __init__(self, user_id, city):
        self.user_id = user_id
        self.city = city


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('sqlite.db')
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def get_user(self, user_id):
        self.cursor.execute('SELECT * FROM USERS WHERE id = ?', (user_id,))
        result = self.cursor.fetchone()
        if result is None:
            return None
        return User(user_id, result[1])

    def create_user(self, user_id):
        self.cursor.execute('INSERT INTO users (id) VALUES (?)', (user_id,))
        self.connection.commit()

    def set_city(self, user_id, city):
        self.cursor.execute('UPDATE users SET city = ? WHERE id = ?', (city, user_id))
        self.connection.commit()
