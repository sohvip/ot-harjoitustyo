import unittest
from level import Play


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.play = Play()

    def test_jump(self):
        self.play.starie_jump()
        self.assertEqual(self.play.starie.jump, 1)

    def test_score(self):
        self.play.spike.sp_x = -51
        self.play.score = 0
        self.play.draw_spikes()
        self.assertEqual(self.play.score, 1)

    def test_spike_move(self):
        self.play.spike.sp_x = -51
        self.play.draw_spikes()
        self.assertEqual(self.play.spike.sp_x, 650)

    def test_background(self):
        self.play.background.bg_x = -640
        self.play.draw_bg()
        self.assertEqual(self.play.background.bg_x, 0)

    def test_speed(self):
        self.play.score = 5
        self.play.speed()
        self.assertEqual(self.play.spike.speed, 1.6)

    def test_starie_action(self):
        self.play.starie.s_y = 317
        self.play.starie_action()
        self.assertEqual(self.play.starie.s_y, 318)

    def test_starie_action_2(self):
        self.play.starie.jump = 1
        self.play.starie_action()
        self.assertEqual(self.play.starie.s_y, 313)
        self.assertEqual(self.play.starie.jumping, 1)

    def test_starie_action_3(self):
        self.play.starie.jump = 1
        self.play.starie.jumping = 41
        self.play.starie_action()
        self.assertEqual(self.play.starie.jumping, 0)
        self.assertEqual(self.play.starie.jump, 0)
