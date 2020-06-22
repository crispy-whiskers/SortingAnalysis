import sorter, timeit

setup = '''
import sorter
import random

s = [random.random() for i in range(10000)]
sort = sorter.Sorter.insertion_sort
'''
print(min(timeit.Timer('a=s[:]; timsort(a)', setup=setup).repeat(7, 1000)))
