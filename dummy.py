import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.2E' % Decimal(height),
                ha='center', va='bottom')

results = {'selection_sort': 2.5229019999999984, 'bubble_sort': 6.371796200000002, 'quick_sort': 0.029005200000000286, 'merge_sort': 0.04052809999999596, 'radix_sort': 3.4195555999999954, 'insertion_sort': 3.137587499999995, 'heap_sort': 0.048856200000003014, 'cycle_sort': 7.412533699999997, 'pigeonhole_sort': 0.0029794000000009646, 'tim_sort': 0.0007918999999958487}
ind = np.arange(len(results.keys()))
fig, ax = plt.subplots()

rects = ax.bar(ind*2, results.values(), .55, color="g")


ax.set_xticklabels(results.keys())
autolabel(rects)
plt.xticks(ind*2, rotation=90)
plt.yticks(np.arange(0, 10, 1))
ax.set_title('Sorting Algorithm Times for n=10000')
plt.ylabel('Seconds')
plt.tight_layout()
plt.show()