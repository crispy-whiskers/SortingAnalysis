import unittest, sorter
def verify_sorted(arr):
        placeholder = 0
        for a in arr:
            if placeholder <= a:
                placeholder = a
                continue
            else:
                return False
        return True
        
class SorterTest(unittest.TestCase):
   def bubble_test(self):
       pass