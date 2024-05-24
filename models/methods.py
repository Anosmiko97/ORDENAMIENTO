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
    
    for i in range(len(lst)):
        num += 1
        j = i - 1
        
        while j >= 0 and lst[i] < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            num += 1
        lst[j + 1] = lst[i] 
    return num
        
def quicksort(arr):
    num = 0
    
    if len(arr) <= 1:
        return num
    else:
        pivot = arr[0]
        
        lesser = []
        for x in arr[1:]:
            if x <= pivot:
                lesser.append(x)
                num += 1
        greater = []
        for x in arr[1:]:
            if x > pivot:
                greater.append(x)
                num += 1
            
        return quicksort(lesser) + [pivot] + quicksort(greater)

def selection_sort(lst):
    num = 0
    
    for i in range(len(lst)):
        num += 1
        
        # Encontrar el elemento mas chico 
        minIndex = i
        for j in range(i+1, len(lst)):
            num += 1
            if lst[j] < lst[min_index]:
                min_index = j
            num += 1

        # Intercambio de valores
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return num

def shellShort(lst):
    num = 0
    
    n = len(lst)
    gap = n // 2 # Intervalo
    
    while gap > 0:
        num += 1
        
        for i in range(gap, n):
            num += 1
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
                lst[j] = temp
                num += 1
            gap //= 2 
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
