import time
from greenlet import greenlet


def task1():
    while True:
        print('task %s >>>>>' % str(1))
        g2.switch()
        time.sleep(0.5)


def task2():
    while True:
        print('task %s >>>>>' % str(2))
        g1.switch()
        time.sleep(0.5)


if __name__ == '__main__':
    g1 = greenlet(task1)
    g2 = greenlet(task2)
    g1.switch()
