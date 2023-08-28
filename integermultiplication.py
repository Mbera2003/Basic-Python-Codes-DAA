def integer_multiplication(x, y):
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        n2 = n // 2

        a = x // 10 ** n2
        b = x % 10 ** n2
        c = y // 10 ** n2
        d = y % 10 ** n2

        ac = integer_multiplication(a, c)
        bd = integer_multiplication(b, d)
        ad_bc = integer_multiplication(a + b, c + d) - ac - bd

        result = ac * 10 ** (2 * n2) + ad_bc * 10 ** n2 + bd
        return result


x = int(input("Enter a number:"))
y = int(input("Enter another number:"))
result = integer_multiplication(x, y)
print(f"The result of {x} * {y} is: {result}")
