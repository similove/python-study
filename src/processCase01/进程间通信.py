import multiprocessing
from time import ctime, sleep


def download_from_web(queue: multiprocessing.Queue):
    data = [11, 22, 33, 44]
    for temp in data:
        if not queue.full():
            sleep(1)
            print(f'生产数据%s到队列中.' % str(temp))
            queue.put(temp)

    print('-- 下载完成并放入到队列中 --')


def analysis_data(queue: multiprocessing.Queue):
    waiting_analysis_data = list()

    while True:
        sleep(2)
        if not queue.empty():
            data = queue.get()
            waiting_analysis_data.append(data)
            print('从队列中获取数据{}放入到处理列表中.'.format(data))
        else:
            break
    print('数据处理完成 %s' % str(waiting_analysis_data))


def main():
    queue = multiprocessing.Queue(4)
    p1 = multiprocessing.Process(target=download_from_web, args=(queue,))
    p2 = multiprocessing.Process(target=analysis_data, args=(queue,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
