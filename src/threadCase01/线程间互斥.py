import threading

g_sum = 0


def adder(num, mutex):
    global g_sum
    for i in range(num):
        mutex.acquire(blocking=True, timeout=100)
        g_sum += 1
        mutex.release()


def main():
    mutex = threading.Lock()
    t1 = threading.Thread(target=adder, args=(1000000, mutex))
    t2 = threading.Thread(target=adder, args=(1000000, mutex))
    t3 = threading.Thread(target=adder, args=(1000000, mutex))
    t4 = threading.Thread(target=adder, args=(1000000, mutex))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print('最后计算的累加结果: %d' % g_sum)


if __name__ == '__main__':
    main()
