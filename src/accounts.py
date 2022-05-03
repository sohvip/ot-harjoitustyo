import sqlite3
from tkinter import messagebox
import os

class Account:
    def __init__(self):
        self.path = self.check_path()
        self.db = sqlite3.connect('self.path')
        self.cursor = self.db.cursor()
        self.create_table()
        
    def check_path(self):
        dirname = os.path.dirname(os.path.abspath(__file__))
        DB_FILENAME = 'accounts.db'
        DB_FILE_PATH = os.path.join(dirname, DB_FILENAME)
        return DB_FILE_PATH
    
    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Accounts (id INTEGER PRIMARY KEY, username TEXT, password TEXT, highscore INTEGER)')
        self.db.commit()

    def new_account(self, username, password):
        self.cursor.execute('SELECT (password) from Accounts WHERE username = ?', (username, ))
        correct = self.cursor.fetchone()
        if correct == None:
            self.cursor.execute('INSERT INTO Accounts (username, password, highscore) VALUES (?, ?, 0)', (username, password))
            self.db.commit()
            messagebox.showinfo('', 'Account created')
            return True
        messagebox.showinfo('', 'Account already exists')
        return False

    # muista tehä ens viikolla!
    #def new_highscore(self, score, account):
        #self.cursor.execute(f'UPDATE Accounts SET highscore = {score} WHERE id = {account}')
        #self.db.commit()
    
    def find_account(self, username, password):
        self.cursor.execute('SELECT (password) from Accounts WHERE username = ?', (username, ))
        correct = self.cursor.fetchone()
        if correct == None:
            messagebox.showinfo('', 'Account not found')
            return False
        compare = correct[0]
        if compare == password:
            return True
        messagebox.showinfo('', 'Wrong password')
        return False

# yee = Account()