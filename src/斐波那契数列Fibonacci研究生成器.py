from collections.abc import Iterable
from collections.abc import Iterator

def fibonacci_1(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print(a)
        a, b = b, a + b
        current_num += 1


def fibonacci_2(all_num):
    '''
    斐波拉契数列生成器
    :param all_num:
    :return:
    '''
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # print(a)
        yield a
        a, b = b, a + b
        current_num += 1


def fibonacci_3(all_num):
    '''
    斐波拉契数列生成器
    :param all_num:
    :return:
    '''
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # print(a)
        yield a
        a, b = b, a + b
        current_num += 1
    return 'GoodJob'


def fibonacci_4(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # print(a)
        r = yield a
        print('>>>>>>> %s' % str(r))
        a, b = b, a + b
        current_num += 1
    return 'GoodJob'


if __name__ == '__main__':
    fibonacci_1(10)
    print('-' * 40)
    # =================================== #
    obj = fibonacci_2(10)
    print(isinstance(obj, Iterable))
    print(isinstance(obj, Iterator))
    for num in obj:
        print(num)
    # =================================== #
    print('-' * 40)
    obj2 = fibonacci_2(10)
    ret1 = next(obj2)
    print(ret1)
    ret2 = next(obj2)
    print(ret2)
    # =================================== #
    print('-' * 40)
    obj3 = fibonacci_2(10)
    while True:
        try:
            ret = next(obj3)
            print(ret)
        except Exception as ret:
            break
    # =================================== #
    print('-' * 40)
    obj4 = fibonacci_3(10)
    while True:
        try:
            ret = next(obj4)
            print(ret)
        except Exception as e:
            print(e.value)
            break
    # =================================== #
    print('-' * 40)
    obj5 = fibonacci_4(10)
    ret5 = next(obj5)
    print(ret5)
    ret6 = next(obj5)
    print(ret6)
    ret7 = obj5.send('Hello')
    print(ret7)
