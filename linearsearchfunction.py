def linear_search(array,n,x):
    for i in range(0, n):
        if array[i] == x:
            return i
    return -1

array = [5, 8, 9, 6, 7]
n= len(array)
x= 9
print(array)
print("element to be found", x)
result = linear_search(array,n,x)
if result==-1:
    print("element not found")
else:
    print("element found at index",result)