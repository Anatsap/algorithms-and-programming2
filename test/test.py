import unittest
from main import wire_legth


class TestWell(unittest.TestCase):
    def test_wire_length(self):
        w =  2
        heights_b = [3, 3, 3]
        expected_cost = 5.66
        result = wire_legth(w, heights_b)
        self.assertAlmostEqual(result, expected_cost, places=2)

    def test_wire_length1(self):
        w =  100
        heights_b = [1, 1, 1, 1]
        expected_cost = 300
        result = wire_legth(w, heights_b)
        self.assertAlmostEqual(result, expected_cost, places=2)


if __name__ == '__main__':
    unittest.main()