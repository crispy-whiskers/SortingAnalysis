import unittest, sorter, random
def verify_sorted(arr):
        placeholder = 0
        for a in arr:
            if placeholder <= a:
                placeholder = a
                continue
            else:
                return False
        return True

sort = sorter.Sorter()

class SorterTest(unittest.TestCase):
    def test_selection(self):
        s = [random.randint(1, 1000) for i in range(10000)]
        l = sort.selection_sort(s)
        self.assertTrue(verify_sorted(l))
    def test_insertion(self):
        s = [random.randint(1, 1000) for i in range(10000)]
        l = sort.insertion_sort(s)
        self.assertTrue(verify_sorted(l))
    def test_bubble(self):
        s = [random.randint(1, 1000) for i in range(10000)]
        l = sort.bubble_sort(s)
        self.assertTrue(verify_sorted(l))
    def test_merge(self):
        s = [random.randint(1, 1000) for i in range(10000)]
        l = sort.merge_sort(s)
        self.assertTrue(verify_sorted(l))
    def test_quick(self):
        s = [random.randint(1, 1000) for i in range(10000)]
        l = sort.quick_sort(s)
        self.assertTrue(verify_sorted(l))
    def test_heap(self):
        s = [random.randint(1, 1000) for i in range(10000)]
        l = sort.heap_sort(s)
        self.assertTrue(verify_sorted(l))
    def test_count(self):
        s = [random.randint(1, 1000) for i in range(10000)]
        l = sort.count_sort(s)
        self.assertTrue(verify_sorted(l))
    def test_radix(self):
        s = [random.randint(1, 1000) for i in range(10000)]
        l = sort.radix_sort(s)
        self.assertTrue(verify_sorted(l))
    def test_bucket(self):
        s = [random.randint(1, 1000) for i in range(10000)]
        l = sort.bucket_sort(s)
        self.assertTrue(verify_sorted(l))
    def test_tim(self):
        s = [random.randint(1, 1000) for i in range(10000)]
        l = s.sort()
        self.assertTrue(verify_sorted(l))
    def test_pigeonhole(self):
        s = [random.randint(1, 1000) for i in range(10000)]
        l = sort.pigeonhole_sort(s)
        self.assertTrue(verify_sorted(l))
    def test_cycle(self):
        s = [random.randint(1, 1000) for i in range(10000)]
        l = sort.cycle_sort(s)
        self.assertTrue(verify_sorted(l))
    def test_binaryinsert(self):
        s = [random.randint(1, 1000) for i in range(10000)]
        l = sort.selection_sort(s)
        self.assertTrue(verify_sorted(l))


if __name__ == '__main__':
    unittest.main()