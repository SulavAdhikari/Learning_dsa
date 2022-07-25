import unittest
from binarytree import Node

class TestBinaryTree(unittest.TestCase):
    def test_basic(self):
        bt = Node(27)
        bt.insert(99)
        bt.insert(76)
        bt.insert(6)
        bt.insert(10)
        bt.insert(2)
        self.assertTrue(bt.exists(27))
        self.assertFalse(bt.exists(1))

if __name__ == '__main__':
    unittest.main()