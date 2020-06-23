def countingSort(arr, exp1): #specialized for radix sort
    n = len(arr) 
    output = [0] * (n) 
  
    count = [0] * (10) 
  
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[ (index)%10 ] += 1
 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ (index)%10 ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1
   
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 

def heapify(arr, n, i): 
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 

    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  
  
        heapify(arr, n, largest)


def partition(arr,low,high):  #quicksort helper
    i = ( low-1 )         
    pivot = arr[high]     
  
    for j in range(low , high): 

        if   arr[j] <= pivot: 

            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
def quickSort(arr,low,high): 
    if low < high: 

        pi = partition(arr,low,high) 
  

        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
        return arr

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  

    L = [0] * (n1) 
    R = [0] * (n2) 
  
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
    i = 0     
    j = 0    
    k = l     
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1

    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
def mergeSort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
    return arr


class Sorter:

    def __init__(self):
        self.tim_sort = list.sort

    def selection_sort(self, arr):
        for i in range(len(arr)): 
            min_idx = i 
            for j in range(i+1, len(arr)): 
                if arr[min_idx] > arr[j]: 
                    min_idx = j 
            arr[i], arr[min_idx] = arr[min_idx], arr[i] 
        return arr

    def bubble_sort(self, arr):
        n = len(arr) 
        for i in range(n-1): 
            for j in range(0, n-i-1): 
                if arr[j] > arr[j+1] : 
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    def quick_sort(self, arr):
        return quickSort(arr, 0, len(arr)-1)

    def merge_sort(self, arr):
        return mergeSort(arr, 0, len(arr)-1)

    def count_sort(self, arr): 

        output = [0 for i in range(256)] 
    
        count = [0 for i in range(256)] 

        ans = ["" for _ in arr] 

        for i in arr: 
            count[ord(i)] += 1
    
        for i in range(256): 
            count[i] += count[i-1] 

        for i in range(len(arr)): 
            output[count[ord(arr[i])]-1] = arr[i] 
            count[ord(arr[i])] -= 1

        for i in range(len(arr)): 
            ans[i] = output[i] 
        return ans

    def radix_sort(self, arr): 
        max1 = max(arr) 
        
        exp = 1
        while max1/exp > 0: 
            countingSort(arr,exp) 
            exp *= 10
        return arr

    def insertion_sort(self, arr): 
        for i in range(1, len(arr)): 
    
            key = arr[i] 
            j = i-1
            while j >= 0 and key < arr[j] : 
                    arr[j + 1] = arr[j] 
                    j -= 1
            arr[j + 1] = key 
        return arr
    
    def heap_sort(self, arr): 
        n = len(arr) 
    
        for i in range(n//2 - 1, -1, -1): 
            heapify(arr, n, i) 
    
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i] # swap 
            heapify(arr, i, 0) 
        return arr
    
    def bucket_sort(self, arr):
            
        x = [] 
        slot_num = 10 
        for i in range(slot_num): 
            x.append([]) 
            
        for j in arr: 
            index_b = int(slot_num * j)  
            x[index_b].append(j) 
        
        for i in range(slot_num): 
            x[i] = self.insertion_sort(x[i]) 
            
        k = 0
        for i in range(slot_num): 
            for j in range(len(x[i])): 
                arr[k] = x[i][j] 
                k += 1
        return arr 
    def cycle_sort(self, arr): 
        writes = 0 
        
        for cycleStart in range(0, len(arr) - 1): 
            item = arr[cycleStart] 
            
            pos = cycleStart 
            for i in range(cycleStart + 1, len(arr)): 
                if arr[i] < item: 
                    pos += 1
            
            if pos == cycleStart: 
                continue
            
            while item == arr[pos]: 
                pos += 1
            arr[pos], item = item, arr[pos] 
            writes += 1
            
            while pos != cycleStart: 
                
                pos = cycleStart 
                for i in range(cycleStart + 1, len(arr)): 
                    if arr[i] < item: 
                        pos += 1
                    
                while item == arr[pos]: 
                    pos += 1
                arr[pos], item = item, arr[pos] 
                writes += 1
            
        return writes
    def pigeonhole_sort(self, arr): 
        my_min = min(arr) 
        my_max = max(arr) 
        size = my_max - my_min + 1

        holes = [0] * size 
    
        for x in arr: 
            assert type(x) is int, "integers only please"
            holes[x - my_min] += 1
        i = 0
        for count in range(size): 
            while holes[count] > 0: 
                holes[count] -= 1
                arr[i] = count + my_min 
                i += 1
        return arr