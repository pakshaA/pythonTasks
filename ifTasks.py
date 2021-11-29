from helpers import read_and_check


def if1():
    a = read_and_check("Введите число: ", output_type="int")
    if a > 0:
        print(f"Число {a} - положительное. Ответ = ", a + 1)
    else:
        print(f"Число {a} - отрицательное или = 0. Ответ = ", a)


def if2():
    a = read_and_check("Введите число: ", output_type="int")
    if a > 0:
        print(f"Число {a} - положительное. Ответ = ", a + 1)
    else:
        print(f"Число {a} - отрицательное или = 0. Ответ = ", a - 2)


def if3():
    a = read_and_check("Введите число: ", output_type="int")
    if a > 0:
        print(f"Число {a} - положительное. Ответ = ", a + 1)
    elif a < 0:
        print(f"Число {a} - отрицательное. Ответ = ", a - 2)
    else:
        print(f"Число {a} = 0. Ответ = ", a == 10)


def if4():
    a, b, c = read_and_check("Введите 3 числа: ", params_count=3, output_type="int")
    counter = 0
    if a > 0:
        counter += 1
    if b > 0:
        counter += 1
    if c > 0:
        counter += 1
    print(f"Количество положительных чисел: {counter}")


def if5():
    a, b, c = read_and_check("Введите 3 числа: ", params_count=3, output_type="int")
    counter = 0
    counter_less_zero = 0
    if a > 0:
        counter += 1
    elif a < 0:
        counter_less_zero += 1
    if b > 0:
        counter += 1
    elif b < 0:
        counter_less_zero += 1
    if c > 0:
        counter += 1
    elif c < 0:
        counter_less_zero += 1
    print(f"Количество положительных чисел: {counter}, количество отрицательных чисел: {counter_less_zero}")


def if6():
    a, b = read_and_check("Введите 2 числа: ", 2, output_type="float")
    if a > b:
        print(f"Большее число - {a}")
    elif a < b:
        print(f"Большее число - {a}")
    else:
        print("Числа равны")


def if7():
    a, b = read_and_check("Введите 2 числа: ", 2, output_type="float")
    if a > b:
        print("Порядковый номер большего числа - 1")
    elif a < b:
        print("Порядковый номер большего числа - 2")
    else:
        print("Числа равны")


def if8():
    a, b = read_and_check("Введите 2 числа: ", 2, output_type="float")
    if a > b:
        print(f"Большее число - {a}, меньшее - {b}")
    elif a < b:
        print(f"Большее число - {b}, меньшее - {a}")
    else:
        print("Числа равны")


def if9():
    a, b = read_and_check("Введите 2 числа: ", 2, output_type="float")
    if a < b:
        print(f"После перераспределения значений переменных A = {a}, B = {a}")
    elif b < a:
        print(f"После перераспределения значений переменных A = {b}, B = {a}")
    else:
        print("Числа равны")


def if10():
    a, b = read_and_check("Введите 2 числа: ", 2, output_type="int")
    if a == b:
        a = b = 0
        print(f"Числа равны. Новые значения A = {a}, B = {b}")
    else:
        a = b = a + b
        print(f"Числа не равны. Новые значения А = {a}, B = {b}")


def if11():
    a, b = read_and_check("Введите 2 числа: ", 2, output_type="int")
    if a != b:
        a = b = max(a, b)
        print(f"Числа не равны, новые значения А = {a}, B = {b}")
    else:
        a = b = 0
        print(f"Числа равны, новые значения А = {a}, B = {b}")


def if12():
    a, b, c = read_and_check("Введите 3 числа: ", 3, output_type="float")
    if b > a < c:
        print(f"Наименьшее число А: {a}")
    elif a > b < c:
        print(f"Наименьшее число B: {b}")
    elif a > c < b:
        print(f"Наименьшее число C: {c}")
    elif a == b < c:
        print(f"Числа А и В равны и являются наименьшими, A = {a}, B = {b}")
    elif a == c < b:
        print(f"Числа А и C равны и являются наименьшими, A = {a}, C = {c}")
    elif c == b < a:
        print(f"Числа B и C равны и являются наименьшими, B = {b}, C = {c}")
    else:
        print("Все числа равны")


def if13():
    a, b, c = read_and_check("Введите 3 числа: ", 3, output_type="float")
    arr = [('a', a), ('b', b), ('c', c)]
    sorted_arr = sorted(arr, key=lambda obj: obj[1])
    average = sorted_arr[1]
    print(f"Среднее число - {average[0]}: {average[1]}")


def if14():
    a, b, c = read_and_check("Введите 3 числа: ", 3, output_type="float")
    arr = [("a", a), ("b", b), ("c", c)]
    sorted_arr = sorted(arr, key=lambda obj: obj[1])
    minimum = sorted_arr[0]
    maximum = sorted_arr[2]
    print(f"Минимальное число - {minimum[0]}: {minimum[1]}", "\n"
          f"Максимальное число - {maximum[0]}: {maximum[1]}")


def if15():
    a, b, c = read_and_check("Введите 3 числа: ", 3, output_type="float")
    arr = [("a", a), ("b", b), ("c", c)]
    sorted_arr = sorted(arr, key=lambda obj: obj[1])
    print(f"Наибольшие числа - {sorted_arr[1][0]} и {sorted_arr[2][0]}.", "\n"
          f"Их значения: {sorted_arr[1][1]} и {sorted_arr[2][1]} ", "\n"
          f"Их сумма = {sorted_arr[1][1] + sorted_arr[2][1]}")


ifTasks = {
    "if1": if1,
    "if2": if2,
    "if3": if3,
    "if4": if4,
    "if5": if5,
    "if6": if6,
    "if7": if7,
    "if8": if8,
    "if9": if9,
    "if10": if10,
    "if11": if11,
    "if12": if12,
    "if13": if13,
    "if14": if14,
    "if15": if15
}
