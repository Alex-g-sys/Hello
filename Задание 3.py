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

# 1. Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.
def division(a, b):
    if b == 0:
        print("Деление на ноль невозможно")
    else:
        result = a / b
        print("Результат деления:", result)

# 2. Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Осуществить вывод
# данных о пользователе одной строкой.

def user_info(name, surname, birth_year, city, email, phone):
    print(f"{name} {surname}, {birth_year} года рождения, проживает в городе {city}. Email: {email}, телефон: {phone}")
# 3. Реализовать функцию my_func(), которая принимает три
# позиционных аргумента и возвращает сумму наибольших двух
# аргументов.
def my_func(a, b, c):
    numbers = [a, b, c]
    numbers.sort(reverse=True)
    return numbers[0] + numbers[1]

# 4. Программа принимает действительное
# положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции
# возведения числа в степень.
def my_func_3(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y < 0:
        result = 1 / result
    return result

# 5. Программа запрашивает у пользователя строку чисел,
# разделённых пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь
# введённых чисел будет добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введён после
# нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.
def my_func_5(x, y):
    sum = 0
    while True:
        input_string = input("Введите числа, разделённые пробелом (или 'q' для выхода): ")
        if input_string == 'q':
            break
        numbers = input_string.split()
        for number in numbers:
            sum += int(number)
        print("Сумма чисел: ", sum)


# 6. Реализовать функцию int_func(), принимающую слова из
# маленьких латинских букв и возвращающую их же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func(word):
    # Возвращаем слово с заглавной первой буквой
    return word.capitalize()


start = True
while start:
    print("1. деление чисел")
    print("2. данные пользователя")
    print("3. три позиционных аргумента и возвращает сумму наибольших двухаргументов")
    print("4. возведение числа x в степень y")
    print("5. сумма введённых чисел")
    print("6. текст с прописной буквы")
    print("7. выход")
    print("___________________________________________________________________________________________________________________________")
    menu_number = enter_number("int")
    if menu_number == 1:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        division(a, b)
    elif menu_number == 2:
        user_info(name="Иван", surname="Иванов", birth_year=1990, city="Москва", email="ivanov@mail.ru",
                  phone="+7 (999) 123-45-67")
    elif menu_number == 3:
        a = get_x()
        b = get_x()
        c = get_x()
        my_func(a, b, c)
    elif menu_number == 4:
            x = get_x()
            y = get_x()
            my_func_3(x, y)
    elif menu_number == 5:
        x = get_x()
        y = get_x()
        my_func_5(x, y)
    elif menu_number == 6:
        word = input("Введите первое число: ")
        int_func(word)
    elif menu_number == 7:
        start = False
    else:
        print("you enter not number 1 of 3")



