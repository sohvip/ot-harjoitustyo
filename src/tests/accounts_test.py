import unittest
import sqlite3
from accounts import Account


class TestAccounts(unittest.TestCase):
    def setUp(self):
        self.account = Account()
    
    def test_check_path(self):
        path = self.account.check_path()
        self.assertEqual(path, '/home/psohvi/ot-harjoitustyo/src/accounts.db')
    
    def test_new_account(self):
        test = self.account.new_account('sohvi', '123')
        self.assertEqual(test, False)
    
    def test_new_account_2(self):
        test = self.account.new_account('umbreon', 'shiny')
        self.account.cursor.execute("DELETE FROM Accounts WHERE username='umbreon'")
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