from math import factorial

menu = '''
Выберите:
1 - Ряд Маклорена e^x
2 - Ряд Маклорена sh(x)
3 - Ряд Маклорена (1 - x) ^ m

0 - Завершение программы'''

def main():
    """Основная функция, включающая в себя меню"""
    n = 100
    while True:
        print(menu)
        choice = input()
        match choice:
            case '1':
                while True:
                    try:
                        x = float(input('Введите X\n'))
                        if abs(x) > 1000:
                            raise ValueError
                    except ValueError:
                        print('Введите число от -1000 до 1000')
                        continue
                    print(f'Результат: {func1(n, x)}')
                    break
            case '2':
                while True:
                    try:
                        x = float(input('Введите X\n'))
                        if abs(x) > 1000:
                            raise ValueError
                    except ValueError:
                        print('Введите число от -1000 до 1000')
                        continue
                    print(f'Результат: {func4(n, x)}')
                    break
            case '3':
                pass
            case '0':
                print('Завершение программы...')
                break
            case _:
                print('Следуйте меню')

def func1(n, x):
    """Нахождение e^x по ряду Маклорена с заданной точностью n"""
    e = 1
    c = 1
    while n:
        e += (x**c)/factorial(c)
        n -= 1
        c += 1
    return e

def func4(n, x):
    """Нахождение sh(x) по ряду Маклорена с заданной точностью n"""
    ch = 0
    c = 1
    while n:
        ch += (x**c)/(factorial(c))
        n -= 1
        c += 2
    return ch

def func10_sup(m, c):
    """Вспомогательная функция для 10 ряда Маклорена
       Возвращает m(m-1)(m-2)...(m-c)"""
    res = 1
    if c == 1:
        return m
    for i in range(c):
        res *= (m-i)
    return res

def func10(n, x, m):
    """Нахождение (1-x)^m по ряду Маклорена с заданной точностью n"""
    func = 1
    sign = True
    c = 1
    while n:
        if sign:
            func -= func10_sup(m, c)/factorial(c) * x**c
        else:
            func += func10_sup(m, c)/factorial(c) * x**c
        n -= 1
        c += 1
        sign = not sign
    return func

main()
