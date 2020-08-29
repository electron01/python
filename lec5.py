list = [1, 5, 6, 2, 12, 9, 0, 2]

print(list)
for i in range(len(list) // 2):  # reverse
    list[i], list[len(list) - 1 - i] = list[len(list) - 1 - i], list[i]
print(list)

list2 = [1, 5, 6, 2, 12, 9, 0, 2]
totalSum = 0
for element in list2:  # Первый Способ
    totalSum += element
print("1)" + str(totalSum))

print("2)" + str(sum(list2)))  # Второй Способ
# i = 0
# while i < len(list2): # Тоже самое с помощью цикла while
#     totalSum += list2[i]
#     i+=1
# print(totalSum)

isNumber = True
list3 = [1, 5, 6, 2, "hello", 12, 9, 0, 2]
for el in list3:
    if type(el) != int:
        isNumber = False
        break

if isNumber:
    print("все значения списка = int")

set1 = set()
set1.add(10)
set1.add(12)
set1.add(10)
set1.add(2)
set1.add("hello")
set1.add("hello")
print(type(set1))
print(set1)

print("remove")
set1.remove("hello")
print(set1)
