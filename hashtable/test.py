from chaining_hashtable import HashMap
import unittest

class TestOpenHashTable(unittest.TestCase):
    def test_basic(self):
        hm = HashMap()
        hm.put(1, 78)
        hm.put(2, 11)
        hm.put(3, 30)
        hm.put(4, 32)
        self.assertEqual(hm.get(1), 78)
        self.assertEqual(hm.get(2), 11)
        self.assertEqual(hm.get(3), 30)
        self.assertEqual(hm.get(4), 32)

    def test_remove(self):
        hm = HashMap()
        hm.put(1, 66)
        hm.put(2, 14)
        hm.remove(1)
        self.assertIsNone(hm.get(1))
        self.assertEqual(hm.get(2), 14)



if __name__ == "__main__":
    unittest.main()