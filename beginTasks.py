def begin1():
    print("Периметр квадрата = ", float(input("Введите сторону квадрата: "))*4)


def begin2():
    print("Площадь квадрата = ", float(input("Введите сторону квадрата: "))**2)


def begin3():
    print("Площадь прямоугольника = ",
          float(input("Введите первую сторону: "))*float(input("Введите вторую сторону: ")))


def begin4():
    print("Длина окружности = ", float(input("Введите диаметр окружности: "))*3.14)


def begin5():
    a = float(input("Введите длину ребра куба: "))
    print("Объем куба = ", a**3, "\n"
          "Площадь поверхности куба = ", 6*(a**2))


def begin6():
    a, b, c = (float(i) for i in input("Введите длины ребер:").split())
    print("Объем прямоугольного параллелепипида = ", a*b*c, "\n" 
          "Площадь его поверхности = ", 2*(a*b+b*c+a*c))


def begin7():
    r = float(input("Введите радиус: "))
    print("Длина окружности = ", 2*3.14*r, "\n"
          "Площадь окружности = ", 3.14*(r**2))


def begin8():
    a, b = (float(i) for i in input("Введите 2 числа: ").split())
    print("Среднее арифметическое = ", (a+b)/2)


def begin9():
    a, b = (float(i) for i in input("Введите 2 числа: ").split())
    print("Среднее геометрическое = ", (a*b)**0.5)


def begin10():
    a, b = (float(i) for i in input("Введите 2 числа: ").split())
    print("Сумма квадратов = ", a**2+b**2, "\n",
          "Разность квадратов = ", a**2-b**2, "\n",
          "Произведение квадратов = ", a**2*b**2, "\n",
          "Частное квадратов = ", a**2/b**2)


def begin11():
    a, b = (float(i) for i in input("Введите 2 числа: ").split())
    print("Сумма модулей = ", abs(a) + abs(b), "\n",
          "Разность модулей = ", abs(a) - abs(b), "\n",
          "Произведение модулей = ", abs(a) * abs(b), "\n",
          "Частное модулей = ", abs(a) / abs(b))


def begin12():
    a, b = (float(i) for i in input("Введите 2 катета: ").split())
    c = (a**2+b**2)**0.5
    print("Гипотенуза = ", c, "\n",
          "Периметр = ", a+b+c)


def begin13():
    r1, r2 = (float(i) for i in input("Введите радиусы кругов: ").split())
    s1 = 3.14*(r1**2)
    s2 = 3.14*(r2**2)
    s3 = s1 - s2
    print("Площадь 1 круга = ", s1, "\n"
          "Площадь 2 круга = ", s2, "\n"
          "Площадь кольца = ", s3)


def begin14():
    length = float(input("Введите длину окружности: "))
    r = length/(2*3.14)
    s = 3.14*(r**2)
    print("Радиус окружности = ", r, "\n"
          "Площадь окружности = ", s)


def begin15():
    s = float(input("Введите площадь круга: "))
    r = (s/3.14)**0.5
    length = 2*3.14*r
    d = 2*r
    print("Диаметр = ", d, '\n'
          "Длина окружности = ", length)


def begin16():
    x1, x2 = (float(i) for i in input("Введите координаты 2х точек: ").split())
    print("Расстояние между точками = ", abs(x2-x1))


def begin17():
    a, b, c = (float(i) for i in input("Введите значения 3х точек: ").split())
    ac = abs(c-a)
    bc = abs(c-b)
    sum_of_two = ac + bc
    print("AC = ", ac, '\n'
          "BC = ", bc, '\n'
          "AC + BC = ", sum_of_two)


def begin18():
    a, b, c = (float(i) for i in input("Введите значения 3х точек: ").split())
    ac = abs(c - a)
    bc = abs(c - b)
    multiplier = ac*bc
    print("Произведение длин отрезков = ", multiplier)


def begin19():
    x1, y1, x2, y2 = (float(i) for i in input("Введите значения 2х координат: ").split())
    length = abs(x2-x1)
    width = abs(y2-y1)
    print("Периметр прямоугольника = ", 2 * length * width, '\n'
          "Площадь прямоугольника = ", length * width)


def begin20():
    x1, y1, x2, y2 = (float(i) for i in input("Введите значения 2х координат: ").split())
    print("Расстояние между точками = ", ((x2-x1)**2+(y2-y1)**2)**0.5)


def begin21():
    x1, y1, x2, y2, x3, y3 = (float(i) for i in input("Введите значения 3х координат: ").split())
    a = ((x2-x1)**2+(y2-y1)**2)**0.5
    b = ((x3-x2)**2+(y3-y2)**2)**0.5
    c = ((x3-x1)**2+(y3-y1)**2)**0.5
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print("Периметр = ", a+b+c, '\n'
          'Площадь = ', s)


def begin22():
    a, b = (str(i) for i in input("Введите содержание 2х переменных: ").split())
    a, b = b, a
    print("После замены переменных местами A = ", a, '\n'
          "B = ", b)


def begin23():
    a, b, c = (str(i) for i in input("Введите содержание 3х переменных: ").split())
    a, b, c = c, a, b
    print("После замены переменных местами A = ", a, '\n'
          "B = ", b, '\n'
          "C = ", c)


def begin24():
    a, b, c = (str(i) for i in input("Введите содержание 3х переменных: ").split())
    a, b, c = b, c, a
    print("После замены переменных местами A = ", a, '\n'
          "B = ", b, '\n'
          "C = ", c)


def begin25():
    x = float(input("Введите значение х: "))
    y = 3 * (x ** 6) - 6 * (x ** 2) - 7
    print("y = ", y)


def begin26():
    x = float(input("Введите значение х: "))
    y = 4*((x-3)**6)-7*((x-3)**3)+2
    print("y = ", y)


def begin27():
    a = float(input("Введите значение А: "))
    print("A^2 = ", a**2, '\n'
          "A^4 = ", a**4, '\n'
          "A^8 = ", a**8)


beginTasks = {
    "begin1": begin1,
    "begin2": begin2,
    "begin3": begin3,
    "begin4": begin4,
    'begin5': begin5,
    "begin6": begin6,
    "begin7": begin7,
    "begin8": begin8,
    "begin9": begin9,
    "begin10": begin10,
    "begin11": begin11,
    "begin12": begin12,
    "begin13": begin13,
    "begin14": begin14,
    "begin15": begin15,
    "begin16": begin16,
    "begin17": begin17,
    "begin18": begin18,
    "begin19": begin19,
    "begin20": begin20,
    "begin21": begin21,
    "begin22": begin22,
    "begin23": begin23,
    "begin24": begin24,
    "begin25": begin25,
    "begin26": begin26,
    "begin27": begin27,
}
