def binary_search(array, x, low, high):
  if low > high:
    return -1
  mid = (low + high) // 2
  if array[mid] == x:
    return mid
  elif array[mid] < x:
    return binary_search(array, x, mid + 1, high)
  else:
    return binary_search(array, x, low, mid - 1)

array = [1, 2, 3, 4, 5]
x = 4
result = binary_search(array, x, 0, len(array) - 1)
if result == -1:
  print("Element not found")
else:
  print("Element found at index", result)
