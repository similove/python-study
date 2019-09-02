a = int(123)
b = str('hello')


class MyClass():
    pass


print(MyClass)

mc = MyClass()
mc_2 = MyClass()

print(mc, type(mc))

print(isinstance(mc, MyClass))
print(isinstance(mc, bool))

print(id(MyClass), type(MyClass))

mc.name = 'zhangsan'
mc_2.name = 'lisi'
print(mc.name)
print(mc_2.name)


class Person1:
    a = 10
    b = 20


p1 = Person1()
p2 = Person1()
print(p1.a, p2.a)


class Person2:
    name = '张三'

    def say_hello(self):
        print(f'你好! 我是%s' % self.name)


p3 = Person2()
p4 = Person2()
p3.name = '李四'
p3.say_hello()
p4.say_hello()
