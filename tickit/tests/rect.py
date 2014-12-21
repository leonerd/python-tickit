
import unittest

from tickit import Rect

class RectTest(unittest.TestCase):
    def setUp(self):
        self.rect = Rect(
            top=5,
            left=10,
            lines=7,
            cols=20
        )

    def test_values(self):
        self.assertEqual(self.rect.top,     5)
        self.assertEqual(self.rect.left,   10)
        self.assertEqual(self.rect.lines,   7)
        self.assertEqual(self.rect.cols,   20)
        self.assertEqual(self.rect.bottom, 12)
        self.assertEqual(self.rect.right,  30)
    @unittest.skip
    def test_linerange(self):
        self.assertEqual(self.rect.linerange, list(range(5, 12)))
        self.assertEqual(self.rect.linerange(8), list(range(8, 12)))
        self.assertEqual(self.rect.linerange(stop=9), list(range(5, 10)))
        self.assertEqual(self.rect.linerange(2, 20), list(range(5, 12)))

    def test_subrect(self):
        sub = self.rect.intersect(Rect(top=0, left=0, lines=25, cols=80))

        self.assertEqual(sub.top,     5)
        self.assertEqual(sub.left,   10)
        self.assertEqual(sub.lines,   7)
        self.assertEqual(sub.cols,   20)
        self.assertEqual(sub.bottom, 12)
        self.assertEqual(sub.right,  30)

        sub = self.rect.intersect(Rect(top=10, left=20, lines=15, cols=60))

        self.assertEqual(sub.top,    10)
        self.assertEqual(sub.left,   20)
        self.assertEqual(sub.lines,   2)
        self.assertEqual(sub.cols,   10)
        self.assertEqual(sub.bottom, 12)
        self.assertEqual(sub.right,  30)

        sub = self.rect.intersect(Rect(top=20, left=20, lines=5, cols=60))

        self.assertIsNone(sub)

