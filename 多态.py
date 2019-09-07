# coding: utf-8


class A:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class B:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


def say_hello1(obj):
    print('你好, %s' % obj.name)


def say_hello2(obj):
    if isinstance(obj, A):
        print('你好, %s' % obj.name)


a = A('孙悟空')
b = B('猪八戒')

say_hello1(a)
say_hello1(b)
say_hello2(a)
say_hello2(b)
