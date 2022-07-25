import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    def test_basic(self):
        q = Queue()
        q.push("A")
        q.push("B")
        q.push("C")
        q.push("D")
        o = q.get_queues()
        self.assertEqual(o, ['A','B','C','D'])
    
    def test_is_empty(self):
        q = Queue()
        q.push("A")
        q.push("B")
        q.push("C")
        q.push("D")
        self.assertFalse(q.is_empty())

    def test_remove(self):
        q = Queue()
        q.push("A")
        q.push("B")
        q.push("C")
        q.push("D")
        q.remove()
        self.assertEqual(q.get_queues(), ['B', 'C', 'D'])

    def test_peek(self):
        q = Queue()
        q.push("A")
        q.push("B")
        q.push("C")
        q.push("D")
        self.assertEqual(q.peek(), "A")

if __name__ == '__main__':
    unittest.main()