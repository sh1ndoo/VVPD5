from math import factorial

menu = '''
Выберите:
1 - Ряд Маклорена e^x
2 - Ряд Маклорена sh(x)
3 - Ряд Маклорена (1 - x) ^ m
4 - Ряд Маклорена sin(x)
5 - Ряд Маклорена cos(x)
6 - Ряд Маклорена ch(x)

0 - Завершение программы'''

def main():
    """
    Основная функция, включающая в себя меню
    :return: None
    """
    n = 100
    while True:
        print(menu)
        choice = input()
        match choice:
            case '1':
                while True:
                    try:
                        x = int(input('Введите X\n'))
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
                        x = int(input('Введите X\n'))
                        if abs(x) > 1000:
                            raise ValueError
                    except ValueError:
                        print('Введите число от -1000 до 1000')
                        continue
                    print(f'Результат: {func4(n, x)}')
                    break
            case '3':
                while True:
                    try:
                        x = float(input('Введите X\n'))
                        m = int(input('Введите M\n'))
                        if abs(x) > 1 or abs(m) > 100:
                            raise ValueError
                    except ValueError:
                        print('Вводите числа x - от -1 до 1 и m от -100 до 100')
                        continue
                    print(f'Результат: {func10(n, x, m)}')
                    break
            case '4':
                while True:
                    try:
                        x = int(input('Введите X\n'))
                        if abs(x) > 1000:
                            raise ValueError
                    except ValueError:
                        print('Введите число от -1000 до 1000')
                        continue
                    print(f'Результат: {func2(n, x)}')
                    break
            case '5':
                while True:
                    try:
                        x = int(input('Введите X\n'))
                        if abs(x) > 1000:
                            raise ValueError
                    except ValueError:
                        print('Введите число от -1000 до 1000')
                        continue
                    print(f'Результат: {func3(n, x)}')
                    break
            case '6':
                while True:
                    try:
                        x = int(input('Введите X\n'))
                        if abs(x) > 1000:
                            raise ValueError
                    except ValueError:
                        print('Введите число от -1000 до 1000')
                        continue
                    print(f'Результат: {func5(n, x)}')
                    break
            case '0':
                print('Завершение программы...')
                break
            case _:
                print('Следуйте меню')

def func1(n:int, x:int) -> float:
    """
    Нахождение e^x по ряду Маклорена с заданной точностью n
    :param n: Точность
    :param x: Аргумент
    :return: Результат вычислений
    """
    e = 1
    c = 1
    while n:
        e += (x**c)/factorial(c)
        n -= 1
        c += 1
    return e

def func4(n:int, x:int) -> float:
    """
    Нахождение sh(x) по ряду Маклорена с заданной точностью n
    :param n: Точность
    :param x: Аргумент
    :return: Результат вычислений
    """
    sh = 0
    c = 1
    while n:
        sh += (x**c)/(factorial(c))
        n -= 1
        c += 2
    return sh

def func10_sup(m:int, c:int) -> int:
    """
    Вспомогательная функция для 10 ряда Маклорена
    :param m: Уменьшаемое
    :param c: Вычитаемое
    :return: m(m-1)(m-2)...(m-c)
    """
    res = 1
    if c == 1:
        return m
    for i in range(c):
        res *= (m-i)
    return res

def func10(n:int, x:float, m:int) -> float:
    """
    Нахождение (1-x)^m по ряду Маклорена с заданной точностью n
    :param n: Точность
    :param x: Аргумент
    :param m: Степень
    :return: Результат вычислений
    """
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

def func2(n:int, x:int) -> float:
    """
    Нахождение sin(x) по ряду Маклорена с заданной точностью n
    :param n: Точность
    :param x: Аргумент
    :return: Результат вычислений
    """
    sin = 0
    c = 1
    sign = False
    while n:
        if sign:
            sin -= (x ** c) / factorial(c)
        else:
            sin += (x ** c) / factorial(c)
        sign = not sign
        n -= 1
        c += 2
    return sin

def func3(n:int, x:int) -> float:
    """
    Нахождение cos(x) по ряду Маклорена с заданной точностью n
    :param n: Точность
    :param x: Аргумент
    :return: Результат вычислений
    """
    cos = 1
    c = 2
    sign = True
    while n:
        if sign:
            cos -= (x ** c) / factorial(c)
        else:
            cos += (x**c)/factorial(c)
        sign = not sign
        n -= 1
        c += 2
    return cos

def func5(n:int, x:int) -> float:
    """
    Нахождение ch(x) по ряду Маклорена с заданной точностью n
    :param n: Точность
    :param x: Аргумент
    :return: Результат вычислений
    """
    ch = 1
    c = 2
    while n:
        ch += (x**c)/factorial(c)
        n -= 1
        c += 2
    return ch

main()
