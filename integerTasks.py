def integer1():
    print("Расстояние в м: ", int(input("Введите расстояние в см: "))//100)


def integer2():
    print("Масса в кг: ", int(input("Введите массу в т: "))//1000)


def integer3():
    print("Размер в килобайтах: ", int(input("Введите размер в байтах: ")) // 1024)


def integer4():
    print("Отрезков В на отрезке А: ", int(input("Введите отрезок А: "))//int(input("Введите отрезок В: ")))


def integer5():
    print("Незанятая часть отрезка А: ", int(input("Введите отрезок А: ")) % int(input("Введите отрезок В: ")))


def integer6():
    a = int(input("Введите двузначное число: "))
    print(f"Кол-во десятков в числе {a} = ", a//10, '\n'
          f"Кол-во единиц в числе {a} = ", a % 10)


def integer7():
    a = int(input("Введите двузначное число: "))
    print(f"Сумма цифр в числе {a} = ", (a//10)+(a % 10), '\n'
          f"Произведение цифр в числе {a} = ", (a//10)*(a % 10))


def integer8():
    a = int(input("Введите двузначное число: "))
    reverse_num = (a//10)+(a % 10)*10
    print(f"Число {a} в перевернутом виде = ", reverse_num)


def integer9():
    a = int(input("Введите трехначное число: "))
    print(f"Кол-во сотен в числе {a} = ", a // 100)


def integer10():
    a = int(input("Введите трехначное число: "))
    print(f"Кол-во единиц в числе {a} = ", a % 10, '\n'
          f"Кол-во десятков в числе {a} = ", a % 100//10)


def integer11():
    a = int(input("Введите трехзначное число: "))
    print(f"Сумма цифр в числе {a} = ", (a % 100//10) + (a % 10) + (a // 100), '\n'
          f"Произведение цифр в числе {a} = ", (a % 100//10) * (a % 10) * (a // 100))


def integer12():
    a = int(input("Введите трехзначное число: "))
    reverse_num = (a % 10)*100 + (a % 100//10)*10 + (a//100)
    print(f"Число {a} в перевернутом виде: ", reverse_num)


def integer13():
    a = int(input("Введите трехзначное число: "))
    remake_num = (a % 100) * 10 + (a//100)
    print(f"Переделанное число {a} = ", remake_num)


def integer14():
    a = int(input("Введите трехзначное число: "))
    remake_num = (a // 10) + (a % 10)*100
    print(f"Переделанное число {a} = ", remake_num)


def integer15():
    a = int(input("Введите трехзначное число: "))
    remake_num = (a % 10) + (a % 100//10)*100 + (a//100) * 10
    print(f"Переделанное число {a} = ", remake_num)


integerTasks = {
    "integer1": integer1,
    "integer2": integer2,
    'integer3': integer3,
    "integer4": integer4,
    "integer5": integer5,
    "integer6": integer6,
    "integer7": integer7,
    "integer8": integer8,
    "integer9": integer9,
    "integer10": integer10,
    "integer11": integer11,
    "integer12": integer12,
    'integer13': integer13,
    "integer14": integer14,
    "integer15": integer15

}
