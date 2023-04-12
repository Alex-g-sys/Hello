# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать
# функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.
list = [False, 'ddd', 3.4e3, (8, 5), [4, 6], "World"] #лист с переменными разных типов
for i in range (len(list)): #цикл с перебором всех элементов циклов
    print(f"Type of variable in the list: {type(list[i])}") #вывод на консоль с указанием типа


# 2. Для списка реализовать обмен значений соседних элементов.Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().
number = int(input("Number of items in the list?: "))
while(number < 0): #проверка, пока пользователь не введёт положителное число
    print('you entered a negative number')
    number = int(input('enter a positive number: '))
list_second = []
for i in range(number): #цикл для вввода списка
    list_second.append(input(f"Enter item : "))
print(f"list:")
print(*list_second, sep = "\n") #вывод списка в консоль
n = len(list_second) - 1 # переменная для длины листа
i = 0 #индекс для цикла
while (i < n): #обход всего списка с шагом 2, чтобы поменять местами соседние элементы
    list_second[i], list_second[i+1] = list_second[i+1], list_second[i]
    i += 2
print(f"Result list:\n", list_second) #вывести список результаты


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени
# года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

list = ['winter', 'spring', 'summer', 'autumn']
dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Enter month number: "))
while(month < 0): #проверка, пока пользователь не введёт положителное число
    print('you entered a negative number')
    month = int(input('enter a positive number: '))
if (month < 12): #проверка выходит ли номер месяца за предел
    if (month > 2 and month < 6): # проверка на время года
        print(f"Result dict:\n", dict.get(2))
        print(f"Result list:\n", list[1])
    elif (month > 5 and month < 9):
        print(f"Result dict:\n", dict.get(3))
        print(f"Result list:\n", list[2])
    elif (month > 8 and month < 12):
        print(f"Result dict:\n", dict.get(4))
        print(f"Result list:\n", list[3])
    else:
        print(f"Result dict:\n", dict.get(1))
        print(f"Result list:\n", list[0])
else:
    print('There is no such month')


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать. Если слово длинное,
# выводить только первые 10 букв в слове.

string_text = input("Enter string: ") #ввод с консоли текста
word = [] #массив отдельных слов без пробела
i = 0 #индекс для цикла
number = 0 #индекс для подсчёта слов и вывода в консоль. Счёт слов в консоли начинается с "1". А к тому же эл-ту в списке мы будем обращаться на 1 меньше
n = string_text.count(' ') + 1 #кол-во пробелов
while (i < n): #проход всех слов в списке
    number = number + 1
    word = string_text.split() #разделение на слова
    print(f" {number} {word[i][0:10]}")# вывод символов. Если больше 10 символов в слове,то на консоль они не выводятся
    i =i + 1 #индес для прогонки цикла