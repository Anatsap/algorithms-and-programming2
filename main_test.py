import unittest
from main_exercise import check_monotonic_array


class TestArrayFuction(unittest.TestCase):
    def test_monoton_increase(self):
        self.assertTrue(check_monotonic_array([1, 2, 3, 4, 5]))

    def test_monoton_decrease(self):
        self.assertTrue(check_monotonic_array([14, 4, 3, 2, 1]))

    def test_not_monoton(self):
        self.assertTrue(check_monotonic_array([1, 5, 48, 30, 57, 90, 56, 100]), (False, [3, 6], [1, 2, 4, 5, 7]))
    
    def test_not_monoton1(self):
        self.assertTrue(check_monotonic_array([67, 54, 48, 89, 78, 15, 14, 100]), (False, [1, 2, 4, 5, 6], [3, 7]))


    
    
if __name__ == '__main__':
    unittest.main()