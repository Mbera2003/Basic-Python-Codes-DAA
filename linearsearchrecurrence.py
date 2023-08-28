def linear_search(L, x, i):
    if i >= len(L):
        return -1
    if L[i] == x:
        return i
    return linear_search(L, x, i + 1)

L = [1, 2, 3, 4, 5, 6, 7]
x = 5
result = linear_search(L, x, 0)
print('List : ', L)
print(f'Element', x,  'is available on index :', result )