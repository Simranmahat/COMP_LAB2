from merge import MergeSort
from merge import Merge
import unittest

class TestMerge(unittest.TestCase):
    def test_merge_asc_sort(self):
        data1 = [12, 10, 11, 9, 2, 1]
        MergeSort(data1,0,len(data1)-1)
        self.assertEqual(data1,[1, 2, 9, 10, 11, 12])
    
    def test_merge_sort_desc_array(self):
        data1 =  [9,7,5,4,1] 
        MergeSort(data1,0,len(data1)-1)
        self.assertEqual(data1,[1,4,5,7,9] )

    def test_insertionnegative(self): #tests for -ve values in list
        data1 = [-12, -10, 11, 9, 2, 1]
        MergeSort(data1,0,len(data1)-1)
        self.assertEqual(data1,[-12, -10, 1, 2, 9, 11])

        

if __name__ == '__main__':
    unittest.main()