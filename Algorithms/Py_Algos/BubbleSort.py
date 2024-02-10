from random import randint

def create_array(h, size):
    return [randint(0, h) for _ in range(size)]

def bubbleSort(arr:list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            try:
                if arr[j] > arr[j+1]:
                    tmp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = tmp
            except IndexError:
                pass

    return arr


if __name__ == "__main__":
    arr = create_array(100, 10)
    arr = bubbleSort(arr)
    print(arr)
