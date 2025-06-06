import unittest
from main import get_min_side
class TestBoardSize(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(get_min_side([2, 3], 10), 9)

    def test_example2(self):
        self.assertEqual(get_min_side([1000000000, 999999999], 2), 1999999998)

    def test_example3(self):
        self.assertEqual(get_min_side([1, 1], 4), 2)

    def test_large_case(self):
        self.assertEqual(get_min_side([5, 5], 100), 50)

if __name__ == '__main__':
    unittest.main()
