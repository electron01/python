for i in range(10):
    print(i)

print("=============")
for i in range(20, -2, -1):
    print(i)

print("==========")

j = 0
while j < 10:
    print(j)
    j += 1

print("===========")
isTest = False
k = 1
while not isTest:
    print(k ** 2)
    k += 1
    if k == 11:
        isTest = True

print("=====Break====")
for i in range(10):
    if i == 6:
        break
    print(i)

print("=====Continue====")
for i in range(10):
    if i == 6:
        continue
    print(i)

print("=================")
for i in range(21, -2, -2):
    print(i)
    if i == 5:
        break
else:
    print("Else!!!")

x = tuple()
print("Type x -> " + str(type(x)))

y = set()
print("Type y -> " + str(type(y)))

z = list()
print("Type z -> " + str(type(z)))

k = {1, 2, 3, 4}
print("Type k -> " + str(type(k)))

h = {}
print("Type h -> " + str(type(h)))
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}  # dict Словарь
print(dict)
print(dict['a'])
print(dict['d'])
dict['a'] = 10
print(dict)
print("===========")

for key, value in dict.items():  # Цикл ддя вывода ключей и значений
    print("KEY:" + str(key) + " Value:" + str(value))


def ex():
    print("Hello")


ex()
ex()
ex()


def swap(list1):
    list1.add(100)


list1 = {1, 2, 3, 4}
print(list1)
swap(list1)
print("list1 after swap")
print(list1)

list222 = [1, 2, 3]
list333 = list222
list333.append(4)
print(list222)

a1 = 2
a2 = a1
a2 = 100
print(a1)


# Задание 1 - есть лист list1 = ["hello", 1, 2, 3, 4, 5, "qwe", 1, - 2, "zxc", 2, 3, "q", 1], нужно на его основе создать словарь, где строки будут ключами, а значениями будет  лист целых чисел
# Пример: ключ "hello, значения - лист [1,2,3,4,5]; ключ "qwe, значения - [1,-2] и тд