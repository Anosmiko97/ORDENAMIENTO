


def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                
def insertion_sort(lst):
    for i in range(len(lst)):
        j = i - 1
        
        while j >= 0 and lst[i] < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = lst[i] 
        
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)

def selection_sort(lst):
    for i in range(len(lst)):
        
        # Encontrar el elemento mas chico 
        minIndex = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        # Intercambio de valores
        lst[i], lst[min_index] = lst[min_index], lst[i]

def shellShort(lst):
    n = len(lst)
    gap = n // 2 # Intervalo
    
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
                lst[j] = temp
            gap //= 2 

def shakerSort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    
    while swapped:
        swapped = False
        
        # Mover hacia la derecha 
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            break
        
        swapped = False
        end -= 1
        
        # Mover hacia la izquierda 
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        start += 1

