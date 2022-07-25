import unittest

from singly_ll import LinkedList
from doubly_ll import LinkedList as DoublyLinkedList, SortedLinkedList


class TestSingly(unittest.TestCase):
    def test_basic(self):
        ll = LinkedList()
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        output = ll.return_str()
        self.assertEqual(output, "123", "should be  123")

    def test_addafter(self):
        ll = LinkedList()
        ll.insert(1)
        ll.insert(2)
        ll.insert(4)
        ll.add_after(after_this=2, to_add=3)
        output = ll.return_str()
        self.assertEqual(output, '1234', "should be 1234")
    
class TestDoubly(unittest.TestCase):
    def test_basic(self):
        ll = DoublyLinkedList()
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        ll.insert(4)
        o = ll.return_forward()
        self.assertEqual(o, "1234", "should be 1234")
    
    def test_addafter(self):
        ll = DoublyLinkedList()
        ll.insert(1)
        ll.insert(2)
        ll.insert(4)
        ll.add_after(2,3)
        o = ll.return_forward()
        self.assertEqual(o, "1234", "should be 1234")
    
    def test_sorted(self):
        ll = SortedLinkedList()
        ll.insert(4)
        ll.insert(3)
        ll.insert(1)
        ll.insert(2)
        o = ll.return_forward()
        self.assertEqual(o, "1234", "should be 1234")

if __name__ == "__main__":
    unittest.main()