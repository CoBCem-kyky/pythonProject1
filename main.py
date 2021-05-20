# name = input(str("Write your Name: "))
# print("Hi,", name+"," + " It's Python")

# while
'''
mathExemple = input("Input math fot calculate or press 'q' to exit ")
while (mathExemple != "q"):
  print("Answer on math: " + mathExemple + " is ", eval(mathExemple))
  mathExemple = input("Input math fot calculate or press 'q' to exit")
'''
# Конструкции if / else / elif
'''
name = input("ВВедите имя")
age = float(input("Ваш возвраст"))
    if age <= 18:
        print("Ты ребенок")
    elif age >= 18 and age <= 30:
        print("Юноша")
     elif age >= 30 and age <= 60:
        print("мужчина")
    else:
        print("Пенсионер")
'''
# Функции пример 1
'''
  def func1(x):
     return x*2
  a = func1(10)
print(a)
'''
#  Функции пример 2
'''
def func2(x, y):
    return x+y
e = func2(4, 5)
     print(e)
    def func3():
    return 5
a = func3()
print(a)
'''
# функция
"""
def calculate_bmi(x, y):
    bmi = y / (x**2)
    print("index mass body " + str(bmi))

    if bmi > 25:
        return "Есть лишний вес"
    else:
        return "нет лишнего веса"

weight = float(input("вес "))
height = float(input("рocт "))
answer = calculate_bmi(height, weight)

print(answer)
"""
# Тестовое задание
"""
def func_num(x):
    if x%2 != 0:
        return str(x) + " не является четным числом"
    else:
        return str(x) + " является четным числом"
num = int(input("Введите число "))
print(func_num(num))
"""

# list - список
'''
 a = [1, 2, 3, 4] # Создаем Список
 print(a)
 a.append(5) # Добавляем в конец пятерку
 print(a)
 a.pop(3) # Удаляем эл-т с индексом 3
 print(a)
 a.pop() # Удаляем последний элемент
 print(a)
 print(a[1]) # Выводим элемент списка с индексом 1(индексы начинаются с 0)
 print(len(a))
'''
# Цикл for
'''
# a = ["hello", "world", "goodbye"]
# for i in a:
#   print(i + " list")


sum = 0
b = [1, 2, 3, 4, 5]
for num in b:
    sum += num #сумма значений в списке
print(sum)  # Если print(sum) будет внутри цикла, то тогда все результаты сложения будут выводится

# заполняем переменными
range(1, 10, 2)
print(list(range(1, 10, 2)))
sum2 = 0
for num2 in range(1, 10, 2):
    sum2 += num2
    print(sum2)
print(sum2)

total_sum = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total_sum +=i
        print(total_sum)
        
'''
# Домашнее задание
'''
total_dz = 1
def func (n, k):
    if n > 20:
        print("n = 0")
    else:
        for i in range(1, n):
           total_dz = total_dz * (i**k)
func(10,2)


def func(n,k):
    total_dz = 0
    for i in range(1, n):
        total_dz = total_dz + i**k
    print(total_dz)

func(5, 2)

sum = 1
b = [1, 2, 3, 4, 5]
for num in range (1, 6):
    sum = sum * num #сумма значений в списке
print(sum)  # Если print(sum) будет внутри цикла, то тогда все результаты сложения будут выводится



def func(n, k):
    if n > 20:
        print("n = 0")
    else:
        total_dz = 0
        for i in range(1, n):
            if i % 2 == 0:
                total_dz = total_dz + i ** k
        print(total_dz)

func(7, 2)
'''
# цикл while and break
'''
total = 0
i1 = 0
while i1 < 6:
    total += i1
    i1 += 1
print(total)
'''
# Пример ниже показывает разницу между while and for, как только в списке
# my_list встречается отрицательное число цикл прерывается в отличии от for
'''
# Пример
my_list = [7, 5, 3, 1, -1, -5, -10, -15, 10]
total = 0
i = 0
while my_list[i] > 0:
    total += my_list[i]
    i += 1
print(total)

# Пример

total1 = 0
for element in my_list:
    if element > 0:
        total1 += element
print(total1)

# Пример

total2 = 0
for element1 in my_list:
    if element1 <= 0:
        break               # break прерывает цикл на отрицательном значении
    total2 += element1
print(total2)

# Пример

total3 = 0
i2 = 0
while total3 < 10 and my_list[i2] > 0:
    total3 += my_list[i2]
    i2 += 1
print(total3)

# Пример

my_list = [7, 5, 3, 1, 100]
total = 0
i = 0
while i < len(my_list) and my_list[i] > 0:
    total += my_list[i]
    i += 1
print(total)

'''
# Домашка 1
'''
my_list = [7, 5, 4, 4, 3, 2, 1, -5, -10, -15, -25, -20]
# while
total_sum = 0
i = -1
while my_list[i] < 0:
    total_sum += my_list[i]
    i-=1
print(total_sum)

# for

total_sum1 = 0
for element in my_list:
   if element > 0:
       element += 1
   else:
       total_sum1 +=element
print(total_sum1)
'''
# Домашка 2
'''
word_list = ["apple", "banana", "grape", "orange", "stop", "hello", "goodbye"]
# while
i = 0
while word_list[i] != "stop":
    print(word_list[i])
    i += 1
    
# for


for element in word_list:
    print(element)
    if element == "stop":
       break
'''

# Вложенные циклы
'''
names = ["Mike", "Tom", "Katy", "Alex"]
n = len(names)
for element in names:
    print(element)
for i in range(n):
    print(names[i])

for i in range(len(names)):
    for j in range(i+1):
        print(names[i])
'''
# dict - Словарь {"Ключ":"Значение"}
'''
d = {"Alex": 25, "Petr" : 37}
print(d)
d["Kate"] = 18
print(d)
d[10] = 20
print(d)
for k, v in d.items():
    print(k)
    print(v)

for key, value in d.items():
    print("Ключ: "+ str(key) + " Значение: " + str(value))
'''
# Домашка
'''
# Задача 1
a = ["first", 1, 2, 3, "second", 10, 20, "third", 100, 110, 120, "fourth", 200]
dict = {}
current_str = None
for e in a:
    if (type(e) == str):
        dict[e] = []
        current_str = e
    else:
        dict[current_str].append(e)
print(dict)

# Задача 2
my_text = "Привет пока как дела привет привет арбуз велосипед стол как слон арбуз да привет"
new_dict = {}
for word in my_text.split():
    if word in new_dict:
        new_dict[word] = new_dict[word] + 1
    else:
        new_dict[word] = 1
print(new_dict)

my_dict2 = {}
for word in my_text.split():
    my_dict2[word] = my_dict2.get(word, 0) + 1
print(my_dict2)
'''
'''
# Многомерные массивы
a = {1, 2, 3, "hello"}

# Объявляем

array_2d = [[1, 2, 3],
            [10, 20, 30],
            [100, 200, 300]]
print(array_2d)
# обратиться к Элементу
print(array_2d[0][2])

array_2d2 = [[1, ],
             [10, 20, 30, 40, 50, 60],
             [100, 200, 300]]
print(array_2d2)

# Выводим многомерные массив в виде матрицы

def print_matrix(array_2d):
    for arr in array_2d:
        print(arr)
print_matrix(array_2d)
'''
'''
def print_matrix(array_2d):
    for arr in array_2d:
        for el in arr:
            print(el, end=' ')
        print()

print_matrix(array_2d)
'''
'''
def print_matrix(array_2d):
    for i in range(len(array_2d)):
        for j in range(len(array_2d[i])):
            print(array_2d[i][j], end=' ')
        print()
print_matrix(array_2d)
'''
# Обновить значение
'''
array_2d[1][1] = 21
print(array_2d)
'''
# Домашка Задача 1
'''
# РАЗОБРАТЬ ПОДРОБНО!!!!!!!!!!!!
def create_2d_array(m, n):
    array_2d = []

    for i in range(m):
        internal_arr = []

        for j in range(n):
            internal_arr.append(0)

        array_2d.append(internal_arr)

    return array_2d

arr_5_10 = create_2d_array(3, 4)
print(arr_5_10)
'''
# Задача 2
# Разобраться внимательно!!!!!
'''
array_2d = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

def swap(arr, i, j):                        # ф-ция замены символов
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def mirror_2d_arr(array_2d):
    for arr in array_2d:
        for i in range(len(arr) // 2):      # вычисляем количество итераций
            swap(arr, i, len(arr) - 1 - i)  # подставляем значения в ф-цию замены

mirror_2d_arr(array_2d)                     # преобразование массива
print(array_2d)
'''
# Генератор списков
'''
a = [1, 2, 3, 4, 5]
b = []
for i in a:
    b.append(i*2)
print(b)

c = [num * 2 for num in a]
print(c)

range3 = [num * 3 for num in range(1,6)]
print(range3)
'''
'''
a = [1, 10, 20, 4, 3, 20, 55]
a_filtered = []
for num in a:
    if num < 10:
        a_filtered.append(num)
print(a_filtered)

a_filter = [num for num in a if num < 10]
print(a_filter)

words = ["hello", "hey", "goodbye", "piono"]
word_filtered = [word for word in words if len(word) < 6] # [word - (временная переменная в word_filtered)
                                                          # for word - (временная переменная в words in words)
                                                          # if len(word) < 6]
print(word_filtered)
'''
# Домашка !!! Задача 1
'''
x = range(10, 1, 2)
list = [num * 2 for num in range(10, 1, -1) if num % 2 == 0]
print(list)
'''
# Домашка !!! Задача 1
'''
words = ["hello", "hey", "goodbye", "piono"]
list_filtered = [word + "." for word in words if len(word) > 5]
print(list_filtered)
'''
# Тип данных Множества (Set)
'''
a = set([1, 10, 5, "hello"])
print(a)
b = set()
print(b)
b.add(1)
print(b)
print(type(b))
'''
'''
list = [1, 2, 3, 1, 1, "hello", "hello"]
my_set = set()
for el in list:
    my_set.add(el)
print(list)
print(my_set)
'''
'''
list_list = [1, 2, 3, 1, 1, "hello", "hello"]
my_set = set(list_list)
print(list_list)
print(my_set)
my_list = list(my_set)
print(my_list)
'''
my_list = [1, 1, 2, 5, 10, 10, 10]
my_set = set(my_list)
summ = 0
for i in my_set:
    summ+=i
print(summ)

print(sum(set(my_list)))