def mergesort(A, low, high):
    if low >= high:
        return
    mid = low + (high - low) // 2
    mergesort(A, low, mid)
    mergesort(A, mid + 1, high)
    merge(A, low, mid, high)


def merge(A, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid

    x = [0] * n1
    y = [0] * n2

    for i in range(0, n1):
        x[i] = A[low + i]
    for j in range(0, n2):
        y[j] = A[mid + j + 1]

    i, j, k = 0, 0, low
    while i < n1 and j < n2:
        if x[i] <= y[j]:
            A[k] = x[i]
            i += 1
        else:
            A[k] = y[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = x[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = y[j]
        j += 1
        k += 1


A = []
n = int(input("Enter the size of the array: "))
for j in range(n):
    element = int(input(f"Enter element {j + 1}: "))
    A.append(element)
print("Unsorted Array:", A)
mergesort(A, 0, n - 1)
print("Sorted Array in Ascending Order:", A)
