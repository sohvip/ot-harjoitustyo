import unittest
import level

class TestLevel(unittest.TestCase):
    def setUp(self):
        pass

    def test_jump(self):
        play=level.Play()
        play.starie_jump()
        self.assertEqual(play.starie.jump,1)

# Testi toimii vain, kun pytest-komentoa kutsuu src-hakemiston
# sisällä komennolla pytest tests.
# Ohte-pajassakin kävin, mutta sielläkään ei saatu toimimaan...
