import unittest

def check_monotonic_array(array):
    is_increase = True
    is_decrease = True
    n = len(array)
    for i in range(0, n - 1):
        if array[i] >= array[i + 1]:
            is_increase = False
        elif array[i] <= array[i + 1]:
            is_decrease = False
    
    return is_increase or is_decrease

class TestArrayFuction(unittest.TestCase):
    def test_monoton_increase(self):
        self.assertTrue(check_monotonic_array([1, 2, 3, 4, 5]))

    def test_monoton_decrease(self):
        self.assertTrue(check_monotonic_array([14, 4, 3, 2, 1]))

    def test_not_monoton(self):
        self.assertFalse(check_monotonic_array([97, 9, 103, 11, 1]))


if __name__ == '__main__':
    unittest.main()

    



   
# print(check_monotonic_array([1, 2, 3, 4, 5]))
# print(check_monotonic_array([5, 4, 3, 2, 1]))
# print(check_monotonic_array([5, 9, 3, 2, 1]))
# print(check_monotonic_array([5, 9, 3, 11, 1]))
# print(check_monotonic_array([23, 56, 90, 102, 203, 290]))