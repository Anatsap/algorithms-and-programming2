import unittest
from avl_priotity_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.queue = PriorityQueue()
        self.queue.put("Task1", 3)
        self.queue.put("Task2", 1)
        self.queue.put("Task3", 2)
        self.queue.put("Task4", 1)
        self.queue.put("Task5", 0)

    def test_order(self):
        self.assertEqual(self.queue.get(), "Task5")
        self.assertEqual(self.queue.get(), "Task2")
        self.assertEqual(self.queue.get(), "Task4")
        self.assertEqual(self.queue.get(), "Task3")
        self.assertEqual(self.queue.get(), "Task1")

    def test_all_queue(self):
        self.queue = PriorityQueue()
        self.queue.put("A", 2)
        self.queue.put("B", 2)
        self.queue.put("C", 1)
        self.assertEqual(self.queue.all_queue(), ["C", "A", "B"])
    def test_empty_get(self):
        empty_queue = PriorityQueue()
        with self.assertRaises(RuntimeError):
            empty_queue.get()
if __name__ == '__main__':
    unittest.main()
