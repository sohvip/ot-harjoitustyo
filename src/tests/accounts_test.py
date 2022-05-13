import unittest
import sqlite3
from accounts import Account


class TestAccounts(unittest.TestCase):
    def setUp(self):
        self.account = Account()

    def test_new_account(self):
        test = self.account.new_account('sohvi', '123')
        self.assertEqual(test, False)

    def test_new_account_2(self):
        test = self.account.new_account('umbreon', 'shiny')
        self.account.cursor.execute(
            "DELETE FROM Accounts WHERE username='umbreon'")
        self.account.database.commit()
        self.assertEqual(test, True)

    def test_find_account(self):
        test = self.account.find_account('sohvi', '123')
        self.assertEqual(test, True)

    def test_find_account_2(self):
        test = self.account.find_account('sohvi', '124')
        self.assertEqual(test, False)

    def test_find_account_3(self):
        test = self.account.find_account('sohva', '123')
        self.assertEqual(test, False)

    def test_check_highscore(self):
        score = self.account.check_highscore(0, 'testi')
        self.assertEqual(score, 1)
    
    def test_check_highscore_2(self):
        score = self.account.check_highscore(5, 'testi')
        self.account.cursor.execute(
            "UPDATE Accounts SET highscore = 1 WHERE username = 'testi'"
        )
        self.account.database.commit()
        self.assertEqual(score, 5)

    def test_get_highscore(self):
        highscore = self.account.get_highscore('testi')
        self.assertEqual(highscore, 1)