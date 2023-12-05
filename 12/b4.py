def is_prime(n, divisor=2):
    if n == 2:
        return True
    elif n <= 1 or n % divisor == 0:
        return False
    elif divisor * divisor > n:
        return True
    else:
        return is_prime(n, divisor + 1)

n = int(input("Введите число: "))
if is_prime(n):
    print("YES")
else:
    print("NO")