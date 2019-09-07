import os
import multiprocessing


def copy_file(q, file_name, old_folder_name, new_folder_name):
    old_f = open(old_folder_name + '/' + file_name, 'rb')
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + '/' + file_name, 'wb')
    new_f.write(content)
    new_f.close()
    q.put(file_name)


def main():
    old_folder_name = input('请输入源文件目录: ')
    try:
        new_folder_name = old_folder_name + '[副本]'
        os.mkdir(new_folder_name)
    except Exception as e:
        print(e)
    file_names = os.listdir(old_folder_name)

    pool = multiprocessing.Pool(5)
    queue = multiprocessing.Manager().Queue()
    for file_name in file_names:
        pool.apply_async(copy_file, args=(queue, file_name, old_folder_name, new_folder_name))

    pool.close()

    all_file_count = len(file_names)
    copy_ok_count = 0
    while True:
        file_name = queue.get()
        print("文件[%s]拷贝完成." % file_name)
        copy_ok_count += 1
        if copy_ok_count >= all_file_count:
            break


if __name__ == '__main__':
    main()
