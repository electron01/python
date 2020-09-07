# num1 = int(input("Enter num1:"))
# num2 = int(input("Enter num2:"))
# if num1 > num2:
#     print("num1>num2")
# elif num2 > num1:
#     print("num2>num1")
# else:
#     print("num1==num2")

# Находим что больше num1 или num2

# Для того чтобы раскомментировать выделите код и нажмите ctr + / (command +c - macOS)
num1 = int(input("Enter num1:"))# Калькулятор
num2 = int(input("Enter num2:"))
op = input("Enter op38(+ - * /):")
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Error")

a = 1
b = 2
a, b = b, a
# python!!
# temp = a
# a = b
# b = temp


# a = a + b
# b = a - b
# a = a - b
# print("a = " + str(a))

# print("b = " + str(b))
# test = True
# test2 = False
# test3 = True
# if (test and test2) or test3:
#     print("test1 test2")
# test = ((5 > 2) and (11 == 12)) or (12 == 12)
# print(test)


# num1 = int(input("Enter num1:"))
# num2 = int(input("Enter num2:"))
# if num1 > 0 and num2 > 0:
#     print("num1 and num2 +")
# elif num1 < 0 and num2 < 0:
#     print("num1 and num2 -")
# elif num1>0 and num2<0:
#     print("num1+ num2-")
# elif num1<0 and num2>0:
#     print("num2 + num1 -")
# print("Hello", end=":")
# print("Hello2")
x = True
print(type(x))
#   list
x = [12, 3, 5, 19, 2, 1, 20, 77, 38, 1]
x.sort()
print(x)
