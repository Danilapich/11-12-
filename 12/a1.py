def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def powerExpression(x, n):
    if n == 0:
        return 1
    else:
        return (x ** n) / factorial(n)

X = int(input("Введите значение числа X: "))
N = int(input("Введите значение числа N: "))

result = powerExpression(X, N)
print("Результат выражения:", result)