import unittest
from merge_sorted_lists import merge_sorted_lists

class ReverseTestCase(unittest.TestCase):
    
    def test_merge_arrays(self):
        self.assertEqual(merge_sorted_lists([1,2,4,5,8],[7,9,15,34,67]),[1, 2, 4, 5, 7, 8, 9, 15, 34, 67])
        self.assertEqual(merge_sorted_lists([1,2,5,7,8],[5,7,9,10]),[1,2,5,7,8,9,10]) 
        self.assertEqual(merge_sorted_lists([1,2,5,7,8],[]),[1,2,5,7,8])
        
if __name__ == "__main__" :
    unittest.main()