import unittest
from game_over import End


class TestGameOver(unittest.TestCase):
    def setUp(self):
        self.end = End(10, 'sohvi')

    def test_final_score(self):
        self.assertEqual(self.end.score, 10)
    
    def test_user(self):
        self.assertEqual(self.end.user, 'sohvi')
