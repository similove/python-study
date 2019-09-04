import gevent
import time
from gevent import monkey

# 为了使用gevent，需要打一个补丁
monkey.patch_all()


def task(name, count):
    for i in range(count):
        print(name, gevent.getcurrent(), i)
        time.sleep(0.0001)
        # gevent.sleep(0.0001)


if __name__ == '__main__':
    g1 = gevent.spawn(task, 'task1', 5)
    g2 = gevent.spawn(task, 'task2', 5)
    g3 = gevent.spawn(task, 'task3', 5)

    g1.join()
    g2.join()
    g3.join()

    print('=' * 40)

    gevent.joinall([
        gevent.spawn(task, 'task4', 5),
        gevent.spawn(task, 'task5', 7),
        gevent.spawn(task, 'task6', 3),
        gevent.spawn(task, 'task7', 9),
        gevent.spawn(task, 'task8', 4)
    ])
