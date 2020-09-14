set1 = {1, 2, 3, 4, 5, 6, 7}
# print(set1[0]) - будет ошибка
set1.add(16)  # Добавление элемента в сет
set1.add(20)
set1.add(1)  # 1 - уже есть в сет( не добавится)
set1.add(32)
set1.add(67)
set1.add(123)
set1.add(256)
for element in set1:
    print(element)
set1.discard(1)
set1.discard(1)
print(set1)

for i in range(10):
    print(i)
    break
else:
    print("else")

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}  # dict Словарь
print(dict)
print(dict['a'])
print(dict['d'])
dict['a'] = 10
print(dict)
print("===========")

for key, value in dict.items():  # Цикл ддя вывода ключей и значений
    print("KEY:" + str(key) + " Value:" + str(value))

# Задание 1 - Создать сет целых чисел, посчитать сумму четных и нечетных чисел
# Задание 2 - есть лист list1 = ["hello", 1, 2, 3, 4, 5, "qwe", 1, - 2, "zxc", 2, 3, "q", 1], нужно на его основе создать словарь, где строки будут ключами, а значениями будет  лист целых чисел
# Пример: ключ "hello, значения - лист [1,2,3,4,5]; ключ "qwe, значения - [1,-2] и тд
