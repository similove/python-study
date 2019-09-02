# coding: utf-8


def sum(a: int, b: int) -> int:
    return a + b


def func1(a, b):
    print(a, "+", b, "=", a + b)


def func2(a):
    a[0] = 20
    print('a = ', a, id(a))


def func3(b, c, *a):
    print("a = ", a, type(a))
    print("b = ", b, type(b))
    print("c = ", c, type(c))


def func4(a, *b, c):
    print("a = ", a, type(a))
    print("b = ", b, type(b))
    print("c = ", c, type(c))


def func5(*a, b, c):
    print("a = ", a, type(a))
    print("b = ", b, type(b))
    print("c = ", c, type(c))


def func6(*, a, b, c):
    print("a = ", a, type(a))
    print("b = ", b, type(b))
    print("c = ", c, type(c))


def func7(a, b, c):
    print("a = ", a, type(a))
    print("b = ", b, type(b))
    print("c = ", c, type(c))
    scope = locals()
    global_scope = globals()
    print(scope)
    print(global_scope)


def sum2(*t):
    s = 0
    for el in t:
        s += el
    return s


if __name__ == '__main__':
    func3(12, 33, 12, 3, 33)
    func4(1, 2, 3, 4, 5, 6, c=7)
    func5(1, 2, 3, 4, 5, b=6, c=7)
    func6(a=1, b=2, c=3)
    # 解包
    t = (11, 22, 33)
    func7(*t)
    d = {'a': 12, 'b': 23, 'c': 34}
    func7(**d)
