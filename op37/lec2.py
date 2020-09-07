# Для того чтобы раскомментировать выделите код и нажмите ctr + / (command +c - macOS)
# for i in range(1, 11):
#     print(i)

# for i in range(20, 0, -1):
#     print(i)

# j=10
# while j!=0:
#     print(j)
#     j

stop = False
while stop != True:
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
a = [3, 5, 20, 2, 21, 1]
print(type(a))
print(a[0])

