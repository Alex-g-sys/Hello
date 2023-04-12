# Задание 1.
# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

# Создание нескольких переменных с разными типами
v_integer = 123
v_float = 4.6e44
v_string = "My project"
v_list = ['i', 75, 4, "prog"]
print(v_integer, v_float, v_string, v_list)#вывод на консоль, созданных переменных

number_int = int(input('Enter an integer: '))# считываем с консоли числа
number_float = float(input('Enter a floating point number : '))
string_str_1 = input('Enter the line: ')# считываем с консоли строки
string_str_2 = input('Enter the line: ')
print("You have entered:", number_int, number_float)# вывод данных на консоль
print("You have entered:", string_str_1, string_str_2)

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате
# чч:мм:сс. Используйте форматирование строк.
seconds_num=int(input())
if (seconds_num >= 0):
    hours=str(seconds_num//3600)
    minutes=(seconds_num//60)%60
    seconds=seconds_num%60
    if minutes<10:
        minutes='0'+str(minutes)
    else:
        minutes=str(minutes)
    if seconds<10:
        seconds='0'+str(seconds)
    else:
        seconds=str(seconds)
    print(f'Time : {hours}:{minutes}:{seconds}')
else:
    print("you entered a negative number")


# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
#первый способ. Без циклов
n = str(input('Enter number: ')) # ввод из консоли, переменная типа string
nn = int(n+n) # вычисление n, приводим переменные к int
nnn = int(n+n+n)
n = int(n)
print(f'Result n+nn+nnn : {n+nn+nnn}') #вывод в консоль результата


#первый способ. С циклами
n1 = str(input('Enter number 2: '))  # ввод из консоли, переменная типа string
i = 0 #индекс для цикла
nn1 = '' #назначаем переменной пустое значение, чтобы определить ей тип string
res1 = 0 #для результата
while (i < 3): #цикл до 3. Задано описании задания
    nn1 = str(n1 + nn1) #делаем из n, nn
    res1 = int(nn1) + res1 #уже считаем часть результата
    i = i + 1 #чтобы цикл походил, и не зациклился
print(f'Result n+nn+nnn : {res1}')
# вывод на консоль результата



# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number = int(input('enter a positive number: ')) #ввод числа
while(number < 0): #проверка, пока пользователь не введёт положителное число
    print('you entered a negative number')
    number = int(input('enter a positive number: '))
max = 0
while number > 0: #в каждом круге цикла, будет отнимать последнюю цифру числа и проверять её
    digit = number % 10 #последняя цифра числа
    if digit > max: #сравниваем число с максимальным на данном моменте
        max = digit #если данное число больше, присваеваем максимальному, цифру на данный момент
    number //= 10
print(max)# вывод наибольшего числа