import unittest

from array_list import ArrayList
 
class TestArraylist(unittest.TestCase):
    def test_add(self):
        AL = ArrayList(size=3)
        AL.add(1)
        AL.add(2)
        AL.add(3)
        o = AL.all()
        self.assertEqual(o, [1,2,3])
    
    def test_delete(self):
        AL = ArrayList(size=5)
        AL.add(1)
        AL.add(2)
        AL.add(3)
        AL.add(4)
        AL.add(5)
        AL.delete(1)
        o = AL.all()
        self.assertEqual(o, [1,3,4,5])
        
    def test__increase_size(self):
        AL = ArrayList(size=3)
        AL.add(1)
        AL.add(2)
        AL.add(3)
        AL._increase_size()
        o = AL.all()
        self.assertEqual(o, [1, 2, 3, None, None, None])

    def test_get(self):
        AL = ArrayList(size=3)
        AL.add(1)
        AL.add(2)
        AL.add(3)

        o = AL.get(1)
        self.assertEqual(o, 2)

if __name__ == '__main__':
    unittest.main()