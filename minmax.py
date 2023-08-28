def max_min(array, n):
    maximum = minimum = array[0]
    for i in range(1,n):
        if array[i]>maximum:
            maximum = array[i]
        elif array[i]<minimum:
            minimum = array[i]
    return maximum , minimum

array=[]
n= int(input("Enter the size of the array:"))
for j in range(n):
    element = int(input(f"Enter element {j+1}: "))
    array.append(element)
maximum, minimum =max_min(array,n)
print("Maximum:", maximum)
print("Minimum:", minimum)