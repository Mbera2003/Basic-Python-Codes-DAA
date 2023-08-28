def partition(array, low, high):
    pivot = array[low]
    i = low+1
    for j in range(low+1, high+1):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i= i+1
    array[low], array[i-1] = array[i-1], array[low]
    return i-1

def quicksort(array, low, high):
    if low<high:
        pvt = partition(array,low,high)
        quicksort(array,low, pvt-1)
        quicksort(array, pvt+1, high)

data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array:")
print(data)
size = len(data)
quicksort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)