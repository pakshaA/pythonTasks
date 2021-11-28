from helpers import read_and_check


def integer1():
    print("Расстояние в м: ", read_and_check("Введите расстояние в см: ", output_type="int")//100)


def integer2():
    print("Масса в кг: ", read_and_check("Введите массу в т: ", output_type="int")//1000)


def integer3():
    print("Размер в килобайтах: ", read_and_check("Введите размер в байтах: ", output_type="int") // 1024)


def integer4():
    print("Отрезков В на отрезке А: ", read_and_check("Введите отрезок А: ", output_type="int") //
          read_and_check("Введите отрезок В: ", output_type="int"))


def integer5():
    print("Незанятая часть отрезка А: ", read_and_check("Введите отрезок А: ", output_type="int") %
          read_and_check("Введите отрезок В: ", output_type="int"))


def integer6():
    a = read_and_check("Введите двузначное число: ", output_type="int")
    print(f"Кол-во десятков в числе {a} = ", a//10, '\n'
          f"Кол-во единиц в числе {a} = ", a % 10)


def integer7():
    a = read_and_check("Введите двузначное число: ", output_type="int")
    print(f"Сумма цифр в числе {a} = ", (a//10)+(a % 10), '\n'
          f"Произведение цифр в числе {a} = ", (a//10)*(a % 10))


def integer8():
    a = read_and_check("Введите двузначное число: ", output_type="int")
    reverse_num = (a//10)+(a % 10)*10
    print(f"Число {a} в перевернутом виде = ", reverse_num)


def integer9():
    a = read_and_check("Введите трехначное число: ", output_type="int")
    print(f"Кол-во сотен в числе {a} = ", a // 100)


def integer10():
    a = read_and_check("Введите трехначное число: ", output_type="int")
    print(f"Кол-во единиц в числе {a} = ", a % 10, '\n'
          f"Кол-во десятков в числе {a} = ", a % 100//10)


def integer11():
    a = read_and_check("Введите трехзначное число: ", output_type="int")
    print(f"Сумма цифр в числе {a} = ", (a % 100//10) + (a % 10) + (a // 100), '\n'
          f"Произведение цифр в числе {a} = ", (a % 100//10) * (a % 10) * (a // 100))


def integer12():
    a = read_and_check("Введите трехзначное число: ", output_type="int")
    reverse_num = (a % 10)*100 + (a % 100//10)*10 + (a//100)
    print(f"Число {a} в перевернутом виде: ", reverse_num)


def integer13():
    a = read_and_check("Введите трехзначное число: ", output_type="int")
    remake_num = (a % 100) * 10 + (a//100)
    print(f"Переделанное число {a} = ", remake_num)


def integer14():
    a = read_and_check("Введите трехзначное число: ", output_type="int")
    remake_num = (a // 10) + (a % 10)*100
    print(f"Переделанное число {a} = ", remake_num)


def integer15():
    a = read_and_check("Введите трехзначное число: ", output_type="int")
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
