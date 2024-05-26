def bubble_sort(lst):
    num = 0
    n = len(lst)
    
    for i in range(n - 1):
        num += 1
        for j in range(0, n - i - 1):
            num += 1
            if lst[j] > lst[j + 1]:
                num += 1
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return num  
              

def insertion_sort(lst):
    num = 0
    
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        num += 1 
        
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            num += 2  
        lst[j + 1] = key 
        num += 1  
    
    return num
    
def quicksort(arr):
    num = 0
    if len(arr) <= 1:
        num += 1
        return num

    pivot = arr[0]
    lesser, equal, greater = [], [], []
    
    for x in arr:
        num += 1
        if x < pivot:
            lesser.append(x)
            num += 1
        elif x > pivot:
            greater.append(x)
            num += 1
        else:
            equal.append(x)
            num += 1

    num_lesser = quicksort(lesser)
    num_greater = quicksort(greater)
    
    num += num_lesser + num_greater

    return num

def selection_sort(lst):
    num = 0
    
    for i in range(len(lst)):
        # Encontrar el elemento más chico
        min_index = i
        for j in range(i + 1, len(lst)):
            num += 1  
            if lst[j] < lst[min_index]:
                min_index = j

        # Intercambio de valores
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]
            num += 1  
    return num


def shellShort(lst):
    num = 0
    n = len(lst)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            num += 1  # 
            
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
                num += 2  
            
            lst[j] = temp
            num += 1  
        
        gap //= 2
        num += 1 
    
    return num


def shakerSort(arr):
    num = 0
    
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    
    while swapped:
        num += 1
        swapped = False
        
        # Mover hacia la derecha 
        for i in range(start, end):
            num += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                num += 1
        
        if not swapped:
            break
        
        swapped = False
        end -= 1
        
        # Mover hacia la izquierda 
        for i in range(end - 1, start - 1, -1):
            num += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                num += 1
        
        start += 1
    return num

