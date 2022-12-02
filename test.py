import unittest
from main import line
class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(line(''), '')