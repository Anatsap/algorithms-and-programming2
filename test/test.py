import unittest
from main import search


class TestBeerFavourites(unittest.TestCase):
    def test_indexes(self):
        result = search("bcb", "bcbcaabaabcbcbb")
        self.assertEqual(result, [0, 9, 11])


if __name__ == '__main__':
    unittest.main()