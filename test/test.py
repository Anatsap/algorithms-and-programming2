import unittest
from main import greedy_set_cover

class TestBeerFavourites(unittest.TestCase):
    def test_min_moves(self):
        self.assertEqual(greedy_set_cover(2, {YN, NY}))

    def test_min_moves1(self):
        self.assertEqual(bfs(10, 7, 3, 0, 7), 5)


if __name__ == '__main__':
    unittest.main()