import sqlite3
from tkinter import messagebox
import os


class Account:
    '''Tietokannasta huolehtiva luokka.'''

    def __init__(self):
        '''Luokan konstruktori. Luo tietokannan.'''
        self.path = self.check_path()
        self.database = sqlite3.connect(self.path)
        self.cursor = self.database.cursor()
        self.create_table()

    def check_path(self):
        '''Selvittää tietokantaan johtavan polun.

        Returns:
            Palauttaa polun muuttujassa path.
        '''
        dirname = os.path.dirname(os.path.abspath(__file__))
        filename = 'accounts.db'
        path = os.path.join(dirname, filename)
        return path

    def create_table(self):
        '''Luo tietokantaan taulun Accounts mikäli sitä ei ole vielä olemassa'''
        text = '(id INTEGER PRIMARY KEY, username TEXT, password TEXT, highscore INTEGER)'
        self.cursor.execute(
            f'CREATE TABLE IF NOT EXISTS Accounts {text}')
        self.database.commit()

    def new_account(self, username, password):
        '''Lisää uuden käyttäjän Accounts-tauluun, jos ehdot täyttyvät.

        Args:
            username: Käyttäjän syöttämä käyttäjänimi.
            password: Käyttäjän syöttämä salasana.

        Returns:
            True, jos saman nimistä käyttäjää ei ole ennen olemassa, muuten False.
        '''
        self.cursor.execute(
            'SELECT (password) from Accounts WHERE username = ?', (username, ))
        correct = self.cursor.fetchone()
        if correct is None:
            self.cursor.execute(
                'INSERT INTO Accounts (username, password, highscore) VALUES (?, ?, 0)',
                (username, password))
            self.database.commit()
            messagebox.showinfo('', 'Account created')
            return True
        messagebox.showinfo('', 'Account already exists')
        return False

    def check_highscore(self, score, username):
        '''Hakee pelaajan ennätyspisteet ja vertaa niitä uusiin pisteisiin.

        Args:
            score: Pelaajan viimeisimmän pelikerran pisteet.
            username: Pelaajan käyttäjänimi.

        Returns:
            Palauttaa pelaajan viimeisimmän pelikerran pisteet,
            jos ne ovat korkeammat kuin pelaajan sen hetkinen ennätys,
            muuten palauttaa pelaajan enätyksen.
        '''
        self.cursor.execute(
            'SELECT (highscore) from Accounts WHERE username = ?', (username, ))
        highscore = self.cursor.fetchone()
        highscore = highscore[0]
        if score > highscore:
            self.new_highscore(score, username)
            return score
        return highscore

    def new_highscore(self, score, username):
        '''Tallentaa pelaajan uudet ennätyspisteet tietokantaan.

        Args:
            score: Pelaajan viimeisimmän pelikerran pisteet.
            username: Pelaajan käyttäjänimi.
        '''
        self.cursor.execute(
            f'UPDATE Accounts SET highscore = {score} WHERE username = "{username}"')
        self.database.commit()

    def get_highscore(self, username):
        '''Hakee tietokannasta pelaajan senhetkiset ennätyspisteet.

        Args:
            username: Pelaajan käyttäjänimi.

        Returns:
            Palauttaa pelaajan senhetkiset ennätyspisteet.
        '''
        self.cursor.execute(
            'SELECT (highscore) from Accounts WHERE username = ?', (username, ))
        highscore = self.cursor.fetchone()
        highscore = highscore[0]
        return highscore

    def find_account(self, username, password):
        '''Etsii käyttäjän Accounts-taulukosta ja katsoo täsmääkö salasana.

        Args:
            username: Käyttäjän syöttämä käyttäjänimi.
            password: Käyttäjän syöttämä salasana.

        Returns:
            False, jos käyttäjää ei löydy tai jos salasana on väärin.
            True, jos käyttäjä on olemassa ja salasana täsmää.
        '''
        self.cursor.execute(
            'SELECT (password) from Accounts WHERE username = ?', (username, ))
        correct = self.cursor.fetchone()
        if correct is None:
            messagebox.showinfo('', 'Account not found')
            return False
        compare = correct[0]
        if compare == password:
            return True
        messagebox.showinfo('', 'Wrong password')
        return False
