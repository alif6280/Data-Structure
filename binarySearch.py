numbers = [45, 12, 78, 3, 56, 24, 67, 9, 34, 10]
print("Original:", numbers)

numbers.sort()
print("Sorted  :", numbers)

def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

target = 34
index = binary_search(numbers, target)

print(f"Searching for {target}: Index =", index)
