def max_min(array, i, j):
    if i==j:
        maximum = minimum = array[i]
        return maximum, minimum
    elif i == j-1:
        if array[i] > array[j]:
            maximum = array[i]
            minimum = array[j]
        else:
            maximum = array[j]
            minimum = array[i]
        return maximum, minimum
    else:
        mid = (i+j) // 2
        max1, min1 = max_min(array, i, mid)
        max2, min2 = max_min(array, mid+1, j)
        maximum = max(max1,max2)
        minimum = min(min1, min2)
        return maximum, minimum

array= []
n= int(input("Enter the size of array:"))
for j in range(n):
    element = int(input(f"Enter element {j+1} :"))
    array.append(element)
maximum, minimum = max_min(array, 0, n-1)
print("Maximum: ",maximum, "Minimum: ",minimum)