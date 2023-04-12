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


#1.  Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.
def write_to_file():
    filename = input("Введите название файла: ")
    with open(filename, "w") as f:
        while True:
            line = input("Введите строку для записи в файл (пустая строка для завершения): ")
            if not line:
                break
            f.write(line + "\n")
    print("Данные успешно записаны в файл", filename)

#2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
def count_lines_and_words(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Читаем все строки файла в список
        for i, line in enumerate(lines):
                words = line.split()  # Разделяем строку на слова
                num_words = len(words)  # Подсчитываем количество слов в строке
                print(f"Строка {i + 1} содержит {num_words} слов и {len(line)} символов.")
        num_lines = len(lines)  # Подсчитываем количество строк в файле
        print(f"Файл содержит {num_lines} строк.")

#3.Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней
# величины дохода сотрудников.
# Открываем текстовый файл с записями о зарплатах
def analyze_salaries():
    # открытие файла и чтение данных
    with open('employees.txt', 'r+', encoding="utf-8") as file:
        data = file.readlines()

    # создание списка сотрудников и окладов
    employees = {}
    for line in data:
        line_data = line.split()
        name = line_data[0]
        salary = float(line_data[1])
        employees[name] = salary

    # проверка окладов сотрудников
    less_than_20k = []
    for name, salary in employees.items():
        if salary < 20000:
            less_than_20k.append(name)

    # вывод фамилий сотрудников с окладом менее 20 тысяч
    if len(less_than_20k) > 0:
        print("Следующие сотрудники имеют оклад менее 20 тысяч:")
        print(', '.join(less_than_20k))
    else:
        print("Нет сотрудников с окладом менее 20 тысяч.")

    # вычисление среднего значения оклада
    total_salary = sum(employees.values())
    average_salary = total_salary / len(employees)
    print("Средний доход сотрудников:", round(average_salary, 2))

#4.Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
def translate_numbers():
    input_filename = input("Введите название входного файла: ")
    output_filename = input("Введите название выходного файла: ")
    with open(input_filename, "r") as f_in, open(output_filename, "w") as f_out:
        for line in f_in:
            if "One" in line:
                line = line.replace("One", "Один")
            elif "Two" in line:
                line = line.replace("Two", "Два")
            elif "Three" in line:
                line = line.replace("Three", "Три")
            elif "Four" in line:
                line = line.replace("Four", "Четыре")
            f_out.write(line)


#5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
def sum_numbers():
    filename = input("Введите название файла: ")
    with open(filename, "w") as f:
        numbers = input("Введите числа через пробел: ")
        f.write(numbers)
    with open(filename, "r") as f:
        numbers = f.read().split()
        numbers = [int(num) for num in numbers]
        total = sum(numbers)
        print(f"Сумма чисел в файле {filename}: {total}")




start = True
while start:
    print("1. Записать в файл")
    print("2. выполнить подсчёт строк и слов в каждой строке")
    print("3. оклады сотрудников")
    print("4. перевести числа")
    print("5. сумма чисел в файле")
    print("6. выход")
    print("___________________________________________________________________________________________________________________________")
    menu_number = enter_number("int")
    if menu_number == 1:
        write_to_file()
    elif menu_number == 2:
        file_path = "C:/Users/Olga/PycharmProjects/Задание_3/text_1.txt" #здесь нужно внести путь к вашему файлу
        count_lines_and_words(file_path)
    elif menu_number == 3:
        analyze_salaries()
    elif menu_number == 4:
        translate_numbers()
    elif menu_number == 5:
        sum_numbers()
    elif menu_number == 6:
        start = False
    else:
        print("you enter not number 1 of 61"
              "")




