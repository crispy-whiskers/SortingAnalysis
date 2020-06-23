import sorter, timeit

setup = '''
import random

s = [random.random() for i in range(10000)]
timsort = list.sort
'''
print(min(timeit.Timer('a=s[:]; timsort(a)', setup=setup).repeat(7, 1000)))
