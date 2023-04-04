n = int(input("num = "))


def is_fibonacci(num):
    if num < 0:
        return False
    elif num == 0 or num == 1:
        return True
    else:
        a, b = 0, 1
        while b < num:
            a, b = b, a + b
        return b == num


print(is_fibonacci(n))