def Calculator():
        num1 = int(input("Enter num1:"))
        num2 = int(input("Enter num1:"))
        operation = input("Chose operation (+ - * /)")
        if operation == "+":
            print(num1 + num2)
        elif operation == "-":
            print(num1 - num2)
        elif operation == "*":
            print(num1 * num2)
        elif operation == "/":
            print(num1 / num2)
        else:
            print("Error")



        if input("Again? y/n") == "n":
            stop = True
            print("Ending...")


# Calculator()
Calculator()

# a = [3, 5, 20]
# print(a)
# a.append(11)
# print(a)
# a.append("Hello")
# print(a)
# a.append([1, 2, 3])
# print(a)
# a.pop()
# print(a)
# print(a[0])
# print(a[4])
# print(a[-1])
# a.pop(1)
# print(a)
# # temp = a[2]
# # a[2] = a[1]
# # a[1] = temp
# a[1], a[2] = a[2], a[1]
# print("============")
# print(a)
#
# for element in a:
#     print(element)
#
# b = [1, 2, 3, 4, 5, 6, 7]
#
# totalSum = 0
# for num in b:
#     totalSum += num
# print("==============")
# print(totalSum)
# print("==============")
# totalSum2 = 0
# for i in range(1, 5):
#     totalSum2 += i
# print(totalSum2)
#
# for elem in range(1, 101):
#     if elem % 3 == 0:
#         print(elem)
#
# # for elem in range(1, 101):
# #     if elem % 3 == 0 or elem % 5 == 0:
# #         print(elem)
#
# print("==========")
#
# total = 0
# i = 0
# while i <= 5:
#     total += i
#     i += 1
# print(total)
#
# myList = [1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -4, -5]  # add 6 forex
# i1 = 0
# total2 = 0
# while i1 < len(myList):
#     if myList[i1] > 0:
#         total2 += myList[i1]
#     i1 += 1
# print(total2)
#
# # while i1 < len(myList):
# #     if myList[i1] < 0:
# #         break
# #     total2 += myList[i1]
# #     i1 += 1
# # print(total2)
# i5 = 0
# while True:
#     if i5 == 6:
#         break
#     print(i5)
#     i5 += 1
# print("==========")
# myList2 = [1, 2, 3, 4, 5, 6, 7]
# for i in range(len(myList2)):
#     print(myList2[i])
# print("==========")
#
# print("==========")
# myList2 = [1, 2, 3, 4, 5, 6, 7]
# for i in range(len(myList2)):
#     for j in range(i + 1):
#         print(myList2[i])
# print("==========")
#
# # arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# arr_2d = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# print(arr_2d[0])
#
# print(arr_2d)
# print("==========")
#
#
# def print_2d(array):
#     for arr in array:
#         print(arr)
#
#
# def print_2dv2(array):
#     for arr in array:
#         for el in arr:
#             print(el, end=' ')
#         print()
#
#
# def print_2dv3(array):
#     for k in range(len(array)):
#         for z in range(len(array[k])):
#             print(array[k][z], end=' ')
#         print()
#
#
# def create2d(n, m):
#     arr = []
#     k = 1
#     for i in range(n):
#         podarr = []
#         for j in range(m):
#             podarr.append(k)
#             k += 1
#         arr.append(podarr)
#     return arr
#
#
# def mirror(array):
#     for i in range(len(array)):
#         for j in range(len(array[i]) // 2):
#             array[i][j], array[i][len(array[i]) - 1 - j] = array[i][len(array[i]) - 1 - j], array[i][j]
#
#
# print_2d(arr_2d)
# print("==========")
# print_2dv2(arr_2d)
#
# print("==========")
# print_2dv3(arr_2d)
#
# arr_2d[1][1] = 100
# print("==========")
# print_2dv3(arr_2d)
# print("==========")
#
# print_2dv3(create2d(5, 5))
# print("==========")
# mirror(arr_2d)
# print_2dv3(arr_2d)
#
# print("==========")
# arr_20d = [[1, 2, 3, 4],
#            [5, 6, 7, 8],
#            [10, 11, 12, 13]]
#
# mirror(arr_20d)
# print_2dv3(arr_20d)
