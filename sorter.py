
class Sorter:
    def verify_sorted(self, list):
        placeholder = 0
        for a in list:
            if placeholder <= a:
                placeholder = a
                continue
            else:
                return False
        return True

    def selection_sort(self, list):
        for i in range(len(list)): 
            min_idx = i 
            for j in range(i+1, len(list)): 
                if list[min_idx] > list[j]: 
                    min_idx = j 
            list[i], list[min_idx] = list[min_idx], list[i] 
        return list
