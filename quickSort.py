def quick_sort(arr):
    if len(arr) <= 1:
        return arr  
    pivot = arr[len(arr) // 2]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

numbers = [7, 3, 9, 1, 4, 8, 2]
print("Original:", numbers)
print("Sorted :", quick_sort(numbers))
