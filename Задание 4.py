def get_x():
    while True:
        try:
            num = float(input("Введите число: "))
            return num
        except ValueError:
            print("Вы ввели не число, попробуйте ещё раз.")



def enter_number(types, string=""):
    while True:
        num = input(string)
        try:
            val = int(num) if types == "int" else float(num)
            if val >= 0:
                return val
            else:
                print("ввели символ, а не число")
        except ValueError:
            print("Неправильно введённое значение ")


#1. Реализовать скрипт на питон, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для
# конкретных значений необходимо запускать скрипт с параметрами
def calculate_salary(hours, rate, bonus):
    return (hours * rate) + bonus

#2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
def print_greater_previous(lst):
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            print(lst[i])


#3.Для чисел в пределах от 20 до 240 найти числа, кратные
# 20 или 21. Решите задание в одну строку.
def list_3():
    print([x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0])


#4.Представлен список чисел. Определите элементы списка,
# не имеющие повторений. Сформируйте итоговый массив чисел,
# соответствующих требованию. Элементы выведите в порядке их
# следования в исходном списке. Для выполнения задания
# обязательно используйте генератор.
def list_4():
    lst = [x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0]
    result = [x for x in lst if lst.count(x) == 1]
    print(result)


#5.Реализовать формирование списка, используя функцию range()
# и возможности генератора. В список должны войти чётные числа
# от 100 до 1000 (включая границы). Нужно получить результат
# вычисления произведения всех элементов списка.
def list_5():
    lst = [x for x in range(100, 1001) if x % 2 == 0]
    print("Сгенерированный список")
    print(lst)
    result = 1
    for x in lst:
        result *= x
    print(result)





start = True
while start:
    print("1. скрипт зарплата")
    print("2. Значение списка больше заданных")
    print("3. числа листа, кратные 20 или 21")
    print("4. элементы списка, не имеющие повторений")
    print("5. произведение всех элементов списка")
    print("6. выход")
    print("___________________________________________________________________________________________________________________________")
    menu_number = enter_number("int")
    if menu_number == 1:
        print("выработка в часах = 160, ставка в час = 200, премия = 5000")
        print("Результат:")
        print(calculate_salary(160, 200, 5000))
    elif menu_number == 2:
        lst = [1, 5, 2, 8, 3, 7, 4]
        print("Лист:")
        print(lst)
        print("Результат:")
        print_greater_previous(lst)
    elif menu_number == 3:
        print("Формируем рандомно лист, и выводим все эл-ты в списке кратные 20 или 21")
        list_3()
    elif menu_number == 4:
            print("Формируем рандомно лист, и выводим все эл-ты в списке не имеющие повторений")
            list_4()
    elif menu_number == 5:
        list_5()
    elif menu_number == 6:
        start = False
    else:
        print("you enter not number 1 of 3")




