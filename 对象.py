# coding: utf-8


class Person:
    # print("XXXX")

    def __init__(self, name):
        self.name = name
        # print("init")

    # name = '孙悟空'

    def say_hello(self):
        print("Hello, I'm %s." % self.name)


class Dog:
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")

    def to_string(self):
        return "name:%s" % self.name


class Rectangle1:
    def __init__(self, width, height):
        self.hidden_width = width
        self.hidden_height = height

    def get_width(self):
        return self.hidden_width

    def get_height(self):
        return self.hidden_height

    def set_width(self, width):
        self.hidden_width = width

    def set_height(self, height):
        self.hidden_height = height

    def get_area(self):
        return self.hidden_height * self.hidden_width


class Rectangle2:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.__height * self.__width


class Person2:
    # print("XXXX")

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def say_hello(self):
        print("Hello, I'm %s." % self.name)


if __name__ == '__main__':
    p1 = Person(name='孙悟空')
    # p1.name = '猪八戒'
    p1.say_hello()
    p2 = Person(name='猪八戒')
    # p1.name = '猪八戒'
    p2.say_hello()

    print(locals())

    dog = Dog("旺财", "1", 'f', "0.89")
    dog.run()
    dog.sleep()
    print(dog.to_string())

    r1 = Rectangle1(3, 5)
    print(r1.get_area())

    r2 = Rectangle2(4, 5)
    print(r2.get_area())

    p2 = Person2('张三')
    p2.name = '李四'
    print(p2.name)
