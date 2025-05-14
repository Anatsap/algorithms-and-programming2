import unittest
from main import kruskals_mst


class TestBeerFavourites(unittest.TestCase):
    def test_indexes(self):
        result = kruskals_mst()
        self.assertEqual(result, [0, 9, 11])


if __name__ == '__main__':
    unittest.main()