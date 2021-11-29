from beginTasks import beginTasks
from integerTasks import integerTasks
from booleanTasks import booleanTasks
from ifTasks import ifTasks
from helpers import merge_dicts

allTasks = merge_dicts(beginTasks, integerTasks, booleanTasks, ifTasks)


while True:
    print("___________________________________________________________")
    print("Для начала работы с кодом введите название требуемой задачи")
    print("Список задач:", '\n'
          "1) begin1 - begin27", '\n'
          "2) integer1 - integer15", '\n'
          "3) boolean1 - boolean15", "\n"
          "4) if1 - if15")
    print("Для завершения работы с кодом введите 'exit'.")
    print("___________________________________________________________")
    taskNumber = input("Введите название задания или 'exit' для выхода: ")
    if taskNumber == 'exit':
        is_exit = input("Вы точно хотите выйти? [Yes/No]: ").lower()
        if is_exit == "yes" or is_exit == "y":
            print("Программа завершена.")
            break
        else:
            continue
    elif taskNumber not in allTasks:
        print("Неизвестная задача! Попробуйте снова.")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        continue
    print("___________________________________________________________")
    allTasks[taskNumber]()
    input("Нажмите Enter чтобы перейти к следующей задаче.")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
