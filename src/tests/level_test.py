import unittest
from level import Play


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.play = Play()

    def test_jump(self):
        self.play.starie_jump()
        self.assertEqual(self.play.starie.jump, 1)

    def test_score(self):
        self.play.spike.x = -51
        self.play.score = 0
        self.play.draw_spikes()
        self.assertEqual(self.play.score, 1)
    
    def test_spike_move(self):
        self.play.spike.x = -51
        self.play.draw_spikes()
        self.assertEqual(self.play.spike.x, 650)