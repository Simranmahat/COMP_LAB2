from Quicksort import quick
import unittest

class TestInsertion(unittest.TestCase):
    def test_merge_sort(self):
        data1 = [12, 10, 11, 9, 2, 1]
        data2 = [1, 2, 9, 10, 11, 12]

        quick(data1,0,len(data1)-1)

        self.assertEqual(data1, data2)
        
    def test_insertionnegative(self): #tests for -ve values in list

        data1 = [-12, -10, 11, 9, 2, 1]
        data2 = [-12, -10, 1, 2, 9, 11]
        quick(data1,0,len(data1)-1)
        self.assertEqual(data1, data2)

        

if __name__ == '__main__':
    unittest.main()