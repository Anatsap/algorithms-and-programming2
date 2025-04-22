import unittest
from exercise import brute_force_greedy_set_cover, parse_input


class TestBeerFavourites(unittest.TestCase):
    def test_min_moves(self):
        employers, sorts = parse_input("20 20","YNN YNY YNY NYY NYY NYN")
        result = brute_force_greedy_set_cover(employers, sorts, 5)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()