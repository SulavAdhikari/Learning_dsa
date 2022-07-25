import unittest
from stack import Stack
class TestStack(unittest.TestCase):

    def test_basic(self):
        s = Stack()
        s.push("A")
        s.push("B")
        s.push("C")
        s.push("D")
        output = s.peek()
        self.assertEqual(output, "D")

    def test_pop(self):
        s = Stack()
        s.push("A")
        s.push("B")
        s.push("C")
        s.push("D")
        s.pop()
        output = s.peek()
        self.assertEqual(output, "C")

    def test_is_empty(self):
        s = Stack()
        s.push("A")
        s.push("B")
        s.push("C")
        s.push("D")
        self.assertFalse(s.is_empty())

if __name__ == "__main__":
    unittest.main()

