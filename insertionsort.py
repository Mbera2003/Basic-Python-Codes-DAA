def insertion_sort(array):
  for i in range(1, len(array)):
    key = array[i]

    j = i - 1
    while j >= 0 and array[j] > key:
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = key

array = [5, 3, 8, 6, 7, 2]
insertion_sort(array)
print(array)
