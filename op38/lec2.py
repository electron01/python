# вывод на консоль цифр от 0 до 9
print("======Task1======")
for i in range(10):
    print(i)
print("======Task1======")

# Тоже самое от 0 до 10 с шагом +1
print("======Task2======")
for i in range(0, 10, +1):
    print(i)
print("======Task2======")

print("======Task3======")
# Цикл while работает пока (j<10)
j = 0
while j < 10:
    print(j)
    j += 1
print("======Task3======")

list1 = [10, 20, 50, 1, 2, 90, 117, 47, 2]
# Вывод значений из листа -> 10, 20,50  и  тд
# Element это просто название переменной
for element in list1:
    print(element)

list1.sort()  # Сортировка по возрастанию
print(list1)
list1.reverse()  # Перевернутый лист

# Кортеж(неизменяемый лист)
tuple1 = (1, 2, 3, 4)
# tuple1[1]=100 - будет ошибка!!! нельзя изменять знач-я

# Set - множество
# 1 - содержит только уникальные элементы
# 2 - нельзя обратиться к элементу по его индексу(не гарантирует порядок)
set1 = {1, 2, 3, 4, 5, 6, 7}
# print(set1[0]) - будет ошибка
set1.add(16)  # Добавление элемента в сет
set1.add(20)
set1.add(1)  # 1 - уже есть в сет( не добавится)
set1.add(32)
set1.add(67)
set1.add(123)
set1.add(256)

set1.discard(1)  # Удаление элемента
set1.discard(1)

set1.remove(2)  # Удаление элемента
# set1.remove(2) - если попробовать удалить элемент, которого нет, с помощью remove - будет ошибка

print(set1)

# Задание 1 - изучить теорию про set
# Задание 2 - Создать сет и заполнить его числами, посчитать сумму всех элементов в сет
# Задание 3 - Создать сет и заполнить его числами, посчитать сумму четных и нечетных чисел

print(set1)
totalSumCh = 0
totalSum = 0
for element in set1:
    if element%2==0:
        totalSum+=element
    else:
        totalSumCh+=element

print(totalSum)
print(totalSumCh)

