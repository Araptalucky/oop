import time
import os

def print_array(arr, highlight=None):
    os.system("cls" if os.name == "nt" else "clear")  # Clears the terminal
    for i, num in enumerate(arr):
        if highlight and i in highlight:
            print(f"\033[91m{num}\033[0m", end=" ")  # Red color for swapping
        else:
            print(num, end=" ")
    print("\n")
    time.sleep(0.5)

def bubble_sort_visual(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            print_array(arr, highlight=[j, j+1])
            if arr[j] > arr[j + 1]:  # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print_array(arr)

# Example usage
numbers = [8, 3, 6, 2, 9, 1]
bubble_sort_visual(numbers)
