def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swaps, array is already sorted
            break
    return arr

# Example usage
numbers = [1, 2, 3, 4, 5, 6]
sorted_numbers = bubble_sort_optimized(numbers)
print("Sorted array:", sorted_numbers)
