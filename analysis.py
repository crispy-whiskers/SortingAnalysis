import sorter, timeit

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
