
import unittest

from tickit.tests.rect import Rect

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Rect)
    return suite

