import sqlite3


class User:
    def __init__(self, user_id, amount: int):
        self.user_id = user_id
        self.amount = amount


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('echo.db')
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def get_user(self, user_id):
        self.cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        result = self.cursor.fetchone()
        if result is None:
            return None
        return User(user_id, result[1])

    def create_user(self, user_id):
        self.cursor.execute('INSERT INTO users(id, amount) VALUES (?,  ?)', (user_id, 1))
        self.connection.commit()

    def set_amount(self, user_id, amount):
        self.cursor.execute('UPDATE users SET amount = ? WHERE id = ?', (amount, user_id))
        self.connection.commit()