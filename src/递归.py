# coding: utf-8


def factorial(n: int) -> int:
    '''
    计算n的阶乘.
    :param n: 阶乘的参数
    :return: n!
    '''
    if n == 1:
        return 1
    return n * factorial(n - 1)


def sum1(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n + sum1(n - 1)


def power(n, i):
    if i == 1:
        return n
    else:
        return n * power(n, i - 1)


def huiWen(s):
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return huiWen(s[1:-1])


def func1(lst):
    newList = []
    for element in lst:
        if element % 2 == 0:
            newList.append(element)
    return newList


def func2(fn, lst):
    newList = []
    for element in lst:
        if fn(element):
            newList.append(element)
    return newList


if __name__ == '__main__':
    print(factorial(10))
    print(sum1(100))
    print(power(2, 20))
    print(huiWen("abcdcba"))
    print(huiWen("abccba"))
    print(huiWen("a"))

    print(huiWen("aa"))
    print(huiWen("aab"))
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    def f(el):
        return el % 2 == 0


    fn = lambda x, y: x + y

    print(func2(f, lst))
    print(list(filter(f, lst)))
    # 匿名函数
    print(func2(lambda element: element > 5, lst))
    print(list(filter(lambda element: element % 3 == 0, lst)))
    print(list(map(lambda x: x ** x, lst)))
    l = ['aa', 'sda', 'frwaeasd', 'dsds', '21342', '0']
    l.sort(key=len, reverse=True)
    print(l)
