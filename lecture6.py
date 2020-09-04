set1 = set()
set1.add(10)
set1.add(12)
set1.add(10)
set1.add(2)
set1.add(11)
set1.add("String")
set1.add(13)
set1.add(15)
set1.add("hello")
set1.add("Hello world")
set1.add("Str555")
for ell in set1: # Проверка делится ли число на 2
    if type(ell) == int and ell % 2 == 0:
        print(ell)

for element in set1:
    if type(element) == str and len(element) > 5: # Вывести строки длинной больше 5 символов
        print(element)

for i in range(10):
    if i == 6:
        break
    print(i)
print("=======")

for i in range(10):
    if i == 6:
        continue
    print(i)
print("=======")

set1.remove(10)# Отличие remove and discard
print(set1)
set1.discard(10)
# set1.remove(10)
print(10)

a = (15, 22, 33,41)

print(a[1:4])

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} #dict Словарь
print(dict)
print(dict['a'])
print(dict['d'])
print("===========")
print(a)

for key, value in dict.items():# Цикл ддя вывода ключей и значений
    print("KEY:" +str(key) +" Value:" +str(value))
