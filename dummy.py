import sorter, random

s = [random.randint(1, 1000) for i in range(10000)]
sort = sorter.Sorter()

sort.radix_sort(s)