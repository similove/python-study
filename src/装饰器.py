import time


# 定义一个计算函数运行时间的装饰器
def run_time_enhance(old):
    def new_fun(*args, **kwargs):
        start = time.time()
        result = old(*args, **kwargs)
        end = time.time()
        print("run time:", end - start)
        return result

    return new_fun


@run_time_enhance
def add(a, b):
    print(a, '+', b, '=', a + b)


@run_time_enhance
def mul(a, b):
    print(a, '*', b, '=', a * b)


if __name__ == '__main__':
    add(1, 2)
    mul(2, 3)
    # enhanced_add = run_time_enhance(add)
    # enhanced_add(2, 5)
    # enhanced_mul = run_time_enhance(mul)
    # enhanced_mul(6, 3)
