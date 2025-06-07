def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None
 
    while low <= high:
        
        iterations += 1
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            high = mid - 1

    return upper_bound, iterations

arr = [2.4, 3.2, 4.5, 10.6, 40.1, 50.0, 80.3]
x = 74.9
upper_bound, iterations = binary_search(arr, x)
print(f"Верхня межа: {upper_bound}, \nкількість ітерацій: {iterations}.")