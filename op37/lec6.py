class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    def get_age(self):
        return self.__age


person1 = Person("Artem", 20)
person2 = Person("Alex", 30)

# person1.set_age(-100)

str1 = "1  asasas sasasas ddfdfd "
print(str1.replace(" ", ""))
print(str1[0])


class A:
    def __init__(self, id):
        self.__id = id

    def adder(self, v):
        return v + self.__id


a = A(10)
b = A(20)
print(a.adder(10))
print(b.adder(10))
