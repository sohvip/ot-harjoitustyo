import unittest
from user_interface.sign_in_rules import not_empty


class TestSignInRules(unittest.TestCase):
    def setUp(self):
        pass

    def test_not_empty(self):
        test = not_empty('', '')
        self.assertEqual(test, False)
    
    def test_not_empty_2(self):
        test = not_empty('a', 'a')
        self.assertEqual(test, True)