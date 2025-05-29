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

    def test_wire_length2(self):
        w =  4
        heights_b = [100, 2, 100, 2, 100]
        expected_cost = 396.32
        result = wire_legth(w, heights_b)
        self.assertAlmostEqual(result, expected_cost, places=2)

    def test_wire_length3(self):
        w = 4
        heights_b = [
            56, 18, 17, 94, 23, 7, 21, 94, 29, 54,
            44, 26, 86, 79, 4, 15, 5, 91, 25, 17,
            88, 66, 28, 2, 95, 97, 60, 93, 40, 70,
            75, 48, 38, 51, 34, 52, 87, 8, 62, 77,
            35, 52, 3, 93, 34, 57, 51, 11, 39, 72
        ]
        expected_cost = 2738.18
        result = wire_legth(w, heights_b)
        self.assertAlmostEqual(result, expected_cost, places=2)


if __name__ == '__main__':
    unittest.main()