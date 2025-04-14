from random import randint

def quicksort(arr, left, right):
    if left < right:
        pivot_position = partition(arr, left, right)
        quicksort(arr, left, pivot_position-1)
        quicksort(arr, pivot_position+1, right)             


def partition(arr, left, right):
    pivot = arr[right]

    i = left

    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[right], arr[i] = arr[i], arr[right]

    return i



arr = [7, 4, 1, 2, 9, 0, 10, 11, 23, 5]

quicksort(arr, 0, len(arr)-1)


print(arr)