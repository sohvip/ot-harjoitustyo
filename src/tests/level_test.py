import unittest
import level

class TestLevel(unittest.TestCase):
    def setUp(self):
        return
    
    def test_level(self):
        level=level()
        self.assertTrue(level)
