# Divide and conquer strategy
# Works by taking a pivot, comparing to the values of the list/array
# Change the value if v <= p
from random import randint
def create_array(h, size):
    return [randint(0, h) for _ in range(size)]

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo -1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    
    tmp = arr[i+1]
    arr[i+1] = arr[hi]
    arr[hi] = tmp

    return i+1


def quicksort(arr, low, high):
    if low < high:
        pIdx = partition(arr, low, high)
        quicksort(arr, low, pIdx -1)
        quicksort(arr, pIdx +1, high)

if __name__ == "__main__":
    arr = create_array(100, 25)
    print("old array:" ,arr)
    quicksort(arr, 0, len(arr) -1)
    print("New Array: ", arr)
