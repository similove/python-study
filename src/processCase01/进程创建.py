from time import ctime, sleep

import multiprocessing


def music(musicName):
    for i in range(3):
        print("I was listening %s, %s" % (musicName, ctime()))
        sleep(1)


def move(moveName):
    for i in range(2):
        print("I was at the %s! %s" % (moveName, ctime()))
        sleep(3)


if __name__ == '__main__':
    t1 = multiprocessing.Process(target=music, args=(u'爱我1中华',))
    t2 = multiprocessing.Process(target=move, args=(u'战狼',))
    t1.start()
    t2.start()
