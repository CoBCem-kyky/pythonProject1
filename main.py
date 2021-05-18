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


