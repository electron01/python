a = [3, 5, 20, 2, 21, 1]
# a[0] = 3, a[1]=5, a[2]=20, a[3]=2, a[4] = 21, a[5]=1
print(a)
print("=====Sort=====")
a.sort()  # Сортировка по возрастанию
print(a)
test = 30.2
print("type test = " + str(type(test)))
# type(x) - возращает тип x
print("=====Revers=====")
a.reverse()  # Перевернутый список(21..1)
print(a)
print("=====len======")
print("length a = " + str(len(a)))
print(a[len(a) - 1])  # last element a[5] = 1
print("=====Append=====")
a.append(11)  # Добавили 11 в список
print(a)
a.append("Hello")  # Добавили "Hello" в список
print(a)
a.append([1, 2, 3])  # Добавили подсписок[1,2,3] в список а
print(a)
a.pop(7)  # Удалили a[7] = Hello из списка а
print(a)
print("=====Print1=====")
for i in range(8):
    print(a[i])  # Здесь меняется переменная i, и поэтому я вывожу a[i], i = 0..1..2..3..4..5..6..7
print("=====Print1=====")

print("=====Print2=====")
for element in a:
    print(element)
# Здесь вывожу сам элемент из списка, element =21,element =20,element =5,element =3,element =2,element =1,element =11, element= [1,2,3]
print("=====Print2=====")

# Считаем Фактариал числа!!!
# Через for и while
# 6! = 1*2*3*4*5*6
# 7! = 1*2*3*4*5*6*7
# FOR!
num = int(input("Enter num:"))
rez = 1
# for i in range(2, num + 1):
#     rez *= i
# print(rez)
# WHILE!
i = 2
while i <= num:
    rez *= i
    i += 1
print(rez)
# 3 Способа поменять значения переменных местами
# 1!
print("=====Swap=====")
# a = 1
# b = 2
# print("a = " + str(a))
# print("b = " + str(b))
# temp = a
# a = b
# b = temp
# print("a = " + str(a))
# print("b = " + str(b))
# 2! Оптимальный вариант!
a = 1
b = 2
print("a = " + str(a))
print("b = " + str(b))
a, b = b, a
print("a = " + str(a))
print("b = " + str(b))
# 3!
# a = 1
# b = 2
# print("a = " + str(a))
# print("b = " + str(b))
# a = a + b
# b = a - b
# a = a - b
# print("a = " + str(a))
# print("b = " + str(b))

#Задание 1
#Создать список с числами и отсортировать его в порядке Убывания!
#Задание 2
#Создать список, заполнить числами, и почитать сумму, всех чисел из списка
#Задание 3
#Создать список, заполнить его  целыми числами(и/или не только  целыми числами), произвести проверку значений, данного списка, если все элементы целые числа вывести(«все значения списка = int»)
#Задание 4
# Создать список, из нескольких целых чисел и нескольких строк, поменять местами первое встреченное число и первую строку местами, в цикле