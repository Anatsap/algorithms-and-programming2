import unittest
from main import kruskals_mst


class TestWell(unittest.TestCase):
    def test_kruskals_mst_basic(self):
        V = 4
        edges = [
            (0, 1, 1),
            (1, 2, 2),
            (0, 2, 3),
            (2, 3, 4),
            (0, 3, 5)
        ]
        expected_cost = 7
        result = kruskals_mst(V, edges)
        self.assertEqual(result, expected_cost)

    def test_simple_graph(self):
        V = 4
        edges = [
            (0, 1, 4),
            (1, 2, 2),
            (0, 2, 3),
            (2, 3, 4)
        ]
        result = kruskals_mst(V, edges)
        expected_cost = 9
        self.assertEqual(result, expected_cost)


if __name__ == '__main__':
    unittest.main()