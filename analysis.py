import sorter, timeit
import numpy as np
import matplotlib.pyplot as plt


setup = '''
import random, sorter

s = [random.randint(1,500) for i in range(10000)]
sort = sorter.Sorter()

'''

sorts = [name for name, val  in sorter.Sorter.__dict__.items() if callable(val)] 
times = []
for alg in sorts:
    print('analyzing '+alg)
    times.append(min(timeit.Timer('a=s[:]; sort.'+alg+'(a)', setup=setup).repeat(5, 1)))

results = {k:v for k,v in zip(sorts, times)}

print(results)
plt.bar(results.keys(), list(results.values()),  width=.5, color='g' )

plt.show()
#{'selection_sort': 2.6578355999999985, 'bubble_sort': 6.620360999999999, 'quick_sort': 0.029759200000000874, 'merge_sort': 0.04239700000000113, 'radix_sort': 3.5414487999999977, 'insertion_sort': 3.260800599999996, 'heap_sort': 0.04982310000001178, 'cycle_sort': 7.771367900000001, 'pigeonhole_sort': 0.003085000000012883, 'tim_sort': 0.0008449999999982083}