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


class Sorter:
    def verify_sorted(self, arr):
        placeholder = 0
        for a in arr:
            if placeholder <= a:
                placeholder = a
                continue
            else:
                return False
        return True

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

    
