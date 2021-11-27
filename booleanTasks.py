def boolean1():
    print("Проверить, является ли число положительным.")
    a = float(input("Введите ваше число: "))
    if a > 0:
        print(f"Число {a} - положительное.")
    elif a == 0:
        print(f"Число {a} не является отрицательным или положительным. ")
    else:
        print(f"Число {a} - отрицательное")


def boolean2():
    print("Проверить нечетность числа А.")
    a = float(input("Введите число : "))
    if a % 2 != 0:
        print(f"Число {a} - нечетное")
    elif a == 0:
        print(f"Число {a} не является четным или четным. ")
    else:
        print(f"Число {a} - четное")


def boolean3():
    print("Проверить четность числа А.")
    a = float(input("Введите число : "))
    if a % 2 != 0:
        print(f"Число {a} - нечетное")
    elif a == 0:
        print(f"Число {a} не является четным или четным. ")
    else:
        print(f"Число {a} - четное")


def boolean4():
    print("Проверить справедливость выражения: А > 2 и B <= 3.")
    a, b = (float(i) for i in input("Введите числа А и Б через пробел: ").split())
    if a > 2 and b <= 3:
        print("Выражение справедливо.")
    else:
        print("Выражение несправедливо")


def boolean5():
    print("Проверить справедливость выражения: А >= 0 и B < -2.")
    a, b = (float(i) for i in input("Введите числа А и Б через пробел: ").split())
    if a >= 0 and b < -2:
        print("Выражение справедливо.")
    else:
        print("Выражение несправедливо")


def boolean6():
    print("Проверить справедливость выражения: A < B < C.")
    a, b, c = (float(i) for i in input("Введите числа А, Б и С через пробел: ").split())
    if a < b < c:
        print("Выражение справедливо.")
    else:
        print("Выражение несправедливо")


def boolean7():
    print("Проверить справедливость выражения: B находится между А и С.")
    a, b, c = (float(i) for i in input("Введите числа А, Б и С через пробел: ").split())
    if a < b < c:
        print("Выражение справедливо.")
    else:
        print("Выражение несправедливо")


def boolean8():
    print("Проверить справедливость выражения: Число А и Б - нечетные.")
    a, b = (float(i) for i in input("Введите числа А и Б через пробел: ").split())
    if a % 2 != 0 and b % 2 != 0:
        print("Выражение справедливо.")
    else:
        print("Выражение несправедливо")


def boolean9():
    print("Проверить справедливость выражения: Число А или Б - нечетные.")
    a, b = (float(i) for i in input("Введите числа А и Б через пробел: ").split())
    if a % 2 != 0 or b % 2 != 0:
        print("Выражение справедливо.")
    else:
        print("Выражение несправедливо")


def boolean10():
    print("Проверить справедливость выражения: Хоть одно из чисел А и В - нечетное.")
    a, b = (float(i) for i in input("Введите числа А и Б через пробел: ").split())
    if (a+b) % 2 != 0:
        print("Выражение справедливо.")
    else:
        print("Выражение несправедливо")


def boolean11():
    print("Проверить справедливость выражения: Числа А и В имеют одинаковую четность.")
    a, b = (float(i) for i in input("Введите числа А и Б через пробел: ").split())
    if (a+b) % 2 != 0:
        print("Выражение справедливо.")
    else:
        print("Выражение несправедливо")


def boolean12():
    print("Проверить справедливость выражения: Каждое из чисел А, В и С - положительное.")
    a, b, c = (float(i) for i in input("Введите числа А, В и С через пробел: ").split())
    if a > 0 and b > 0 and c > 0:
        print("Выражение справедливо.")
    else:
        print("Выражение несправедливо")


def boolean13():
    print("Проверить справедливость выражения: Хотя бы одно из чисел А, В и С - положительное.")
    a, b, c = (float(i) for i in input("Введите числа А, В и С через пробел: ").split())
    if a > 0 or b > 0 or c > 0:
        print("Выражение справедливо.")
    else:
        print("Выражение несправедливо")


def boolean14():
    print("Проверить справедливость выражения: Только одно из чисел А, В и С - положительное.")
    a, b, c = (float(i) for i in input("Введите числа А, В и С через пробел: ").split())
    if a > 0 and b < 0 and c < 0:
        print("Выражение справедливо.")
    elif b > 0 and c < 0 and a < 0:
        print("Выражение справедливо.")
    elif c > 0 and a < 0 and b < 0:
        print("Выражение справедливо.")
    else:
        print("Выражение несправедливо")


def boolean15():
    print("Проверить справедливость выражения: Только два из чисел А, В и С - положительное.")
    a, b, c = (float(i) for i in input("Введите числа А, В и С через пробел: ").split())
    if (a > 0 and b > 0 and c < 0) or (a > 0 and c > 0 and b < 0):
        print("Выражение справедливо.")
    elif b > 0 and a < 0 and c > 0:
        print("Выражение справедливо.")
    else:
        print("Выражение несправедливо")


booleanTasks = {
    "boolean1": boolean1,
    "boolean2": boolean2,
    "boolean3": boolean3,
    "boolean4": boolean4,
    "boolean5": boolean5,
    "boolean6": boolean6,
    "boolean7": boolean7,
    "boolean8": boolean8,
    "boolean9": boolean9,
    "boolean10": boolean10,
    "boolean11": boolean11,
    "boolean12": boolean12,
    "boolean13": boolean13,
    "boolean14": boolean14,
    "boolean15": boolean15
}