import sorter, timeit
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
n = 10000
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.2E' % Decimal(height),
                ha='center', va='bottom')

setup = '''
import random, sorter

s = [random.randint(1,500) for i in range({})]
sort = sorter.Sorter()

'''.format(n)

sorts = [name for name, val  in sorter.Sorter.__dict__.items() if callable(val)] 
times = []
for alg in sorts:
    print('analyzing '+alg)
    times.append(min(timeit.Timer('a=s[:]; sort.'+alg+'(a)', setup=setup).repeat(5, 1)))

results = {k:v for k,v in zip(sorts, times)}

print(results)

avg = sum(times)/len(times)

print('Average: '+str(avg))

ind = np.arange(len(results.keys()))
fig, ax = plt.subplots()
rects = ax.bar(ind*2, results.values(), .55, color="g")
ax.set_xticklabels(results.keys())
autolabel(rects)
plt.xticks(ind*2, rotation=90)
plt.yticks(np.arange(0, 10, 1))
ax.set_title('Sorting Algorithm Times for n='+str(n))
plt.ylabel('Seconds')
plt.tight_layout()
plt.show()

