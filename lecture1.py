# String str
# Привет
name = " "
x = "30"
# int
age = "30"
# float
test = 33.5
# boolean
isActive = False
print("Hello " + name + "Hello")
print(age + "Hello")
number1 = 20
number2 = 6
number3 = number1 ** number2
# + - * / // % ** =-
print(number3)

# print ("test:" + age)
# print("test:" + str(age))

if 5 > 3:
    print("5>3")
    print("hello")
else:
    print("5<3")
    print("1")

num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
if num1 > num2:
    print(str(num1) + ">" + str(num2))
# input str
if num1 > num2:
    print(str(num1) + ">" + str(num2))
if num1 < num2:
    print(str(num1) + "<" + str(num2))
if num1 == num2:
    print(str(num1) + "=" + str(num2))

isTest1 = True
isTest2 = False
isTest3 = True
# and(&) or(|)
if isTest1 & isTest2 & isTest3:
    print("YES")


num1 = int(input("Enter num1:"))
# str(num1)

for i in range(7):
    print(i**2)
j = 1
while j <= 100:
    print(j ** 2)
    j = j + 10


def function():
    print("Function")



function()


def addition(a, b):
    return a + b


print(addition(5, 3))


