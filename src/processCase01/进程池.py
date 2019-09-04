from time import sleep, time

import multiprocessing
import os
import random
import threading





def worker(msg):
    t_start = time()
    print('%s开始执行，进程号为%d' % (msg, os.getpid()))
    sleep(random.random() * random.random() * random.random() * 50)
    t_stop = time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))


def main():
    pool = multiprocessing.Pool(5)
    mutex = threading.Lock()
    mutex.acquire()
    mutex.release()
    for i in range(20):
        pool.apply_async(worker, ("message->[%d]" % i,))
    print('----- start -----')
    pool.close()
    pool.join()
    print('------ end ------')


if __name__ == '__main__':
    main()
