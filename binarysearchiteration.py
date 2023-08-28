def binary_search(array, x):
  low = 0
  high = len(array) - 1
  while low <= high:
    mid = (low + high) // 2
    if array[mid] == x:
      return mid
    elif array[mid] < x:
      low = mid + 1
    else:
      high = mid - 1
  return -1

array = [1, 2, 3, 4, 5]
x = 3
result = binary_search(array, x)
if result == -1:
  print("Element not found")
else:
  print("Element found at index", result)