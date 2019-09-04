import time


def task(name):
    while True:
        print('task %s >>>>>' % str(name))
        time.sleep(0.5)
        yield


def main():
    t1 = task(1)
    t2 = task(2)
    while True:
        next(t1)
        next(t2)


if __name__ == '__main__':
    main()
