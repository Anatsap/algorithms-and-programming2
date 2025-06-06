import unittest
from main import search

class TestKMP(unittest.TestCase):

    def test_no_match(self):
        self.assertEqual(search("xyz", "abcdefgh"), [])

    def test_full_match(self):
        self.assertEqual(search("abc", "abc"), [0])

    def test_multiple_overlaps(self):
        self.assertEqual(search("aaa", "aaaaaa"), [0, 1, 2, 3])

    def test_end_match(self):
        self.assertEqual(search("end", "start middle end"), [13])

if __name__ == '__main__':
    unittest.main()
