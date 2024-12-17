from math import factorial


def main():
    while True:
        pass

def func1(n, x):
    e = 1
    c = 1
    while n:
        e += (x**c)/factorial(c)
        n -= 1
        c += 1
    return e


def func4(n, x):
    ch = 0
    c = 1
    while n:
        ch += (x**c)/(factorial(c))
        n -= 1
        c += 2
    return ch

print(func4(1000, 1))
