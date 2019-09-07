# coding: utf-8


class Animal:
    def __init__(self, name):
        self._name = name

    def run(self):
        print("animal run ...")

    def sleep(self):
        print("animal sleep...")

    def dark(self):
        print("animal dark...")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name)
        self._age = age

    def dark(self):
        print("dog dark...")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


class A(Dog, Animal):
    pass


if __name__ == '__main__':
    dog = Dog('秦桧', 592)
    dog.sleep()
    dog.run()
    dog.dark()
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(issubclass(Dog, object))
    print('--------------')
    print(A.__bases__)
