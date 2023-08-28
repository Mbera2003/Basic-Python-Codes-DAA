array = [5, 8, 9, 6, 7]
n= len(array)
x= 9
print(array)
print("element to be found", x)
for i in range (0, n):
    if array[i] == x:
        print("element found at index", i)