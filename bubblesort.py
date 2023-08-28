def bubble_sort(array):
  n = len(array)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]

array = [5, 3, 8, 6, 7, 2]
bubble_sort(array)
print(array)