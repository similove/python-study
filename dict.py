# coding: utf-8


def fn1(a, b, c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)


# 指定参数类型
def fn2(a: int) -> None:
    print('a = ', a)


# 不定长参数
def fn3(*numbers: int) -> int:
    result = 0
    for el in numbers:
        result += el
    return result


def fn4(a, b, *c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)


def fn5(a, *b, c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)


def fn6(*a, b, c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)


def fn7(*, a, b, c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)


def fn8(**a):
    print(a, type(a))


def fn9(a: int, b: int, **c: int) -> int:
    '''
    :param a: 参数1
    :param b: 参数2
    :param c: 参数3
    :return: 没有返回值
    '''
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))


def sum1(a: int, b: int, c: int) -> int:
    return a + b + c


def fn10():
    def fn():
        return 1

    return fn


ax = 123


def fn11():
    global ax
    ax = 121

    print(ax)


if __name__ == '__main__':
    b = 123
    fn2(b)
    print(fn3(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(fn3(*range(0, 10)))
    fn4(1, 2, 3, 4, 5)
    fn5(1, 2, 3, 4, c=5)
    fn6(1, 2, 3, b=4, c=5)
    fn7(a=1, b=2, c=3)
    fn8(a=123, b='abc', c=321)
    fn9(a=1, b=3, d=9, f=123)

    # 解包
    t = (1, 2, 3)
    fn1(*t)
    d = {'a': 12, 'b': 33, 'c': 123}
    fn1(**d)

    print(fn10()())

    fn11()

    print(ax)
    print(locals())
