from beginTasks import beginTasks
from integerTasks import integerTasks
from booleanTasks import booleanTasks
from helpers import merge_dicts

allTasks = merge_dicts(beginTasks, integerTasks, booleanTasks)

print("___________________________________________________________")
print("Для начала работы с кодом введите название требуемой задачи")
print("Список задач:", '\n'
      "1) begin1 - begin27", '\n'
      "2) integer1 - integer15", '\n'
      "3) boolean1 - boolean15")
print("Для завершения работы с кодом введите 'exit'.")

while True:
    print("___________________________________________________________")
    taskNumber = input("Введите название задания: ")
    if taskNumber == 'exit':
        print("Программа завершена.")
        break
    elif taskNumber not in allTasks:
        print("Неизвестная задача! Попробуйте снова.")
        continue
    print("___________________________________________________________")
    allTasks[taskNumber]()
