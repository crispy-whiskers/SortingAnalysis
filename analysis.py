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
#plt.bar(results.keys(), list(results.values()),  width=.5, color='g' , bottom=.3)
fig, ax = plt.subplots()
#ax.set_xticks(rotation=45)
ax.set_xticklabels(results.keys())
rects = ax.bar(range(len(results.values())), results.values(), .35, color="g", bottom=.4)
plt.xticks(rotation=45)
ax.set_title('Sorting Algorithm Times for n=10000')
plt.show()
