import unittest
from start import Start


class TestStart(unittest.TestCase):
    def setUp(self):
        self.start = Start('sohvi')

    def test_starie_attributes(self):
        self.assertEqual(self.start.starie.s_y, 318)
        self.assertEqual(self.start.starie.jump, 0)
        self.assertEqual(self.start.starie.fall, 1)
        self.assertEqual(self.start.starie.jumping, 0)
