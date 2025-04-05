import unittest
from main import bfs

class TestMoveKnight(unittest.TestCase):
    def test_min_moves(self):
        self.assertEqual(bfs(8, 7, 0, 0, 7), 6)

    def test_min_moves1(self):
        self.assertEqual(bfs(10, 7, 3, 0, 7), 5)


if __name__ == '__main__':
    unittest.main()