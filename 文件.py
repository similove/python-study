# coding: utf-8


class MyException(Exception):
    pass


def read_demo1():
    file_content = ''
    file_name = '文件.py'
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            chunk = 100
            while True:
                content = file.read(chunk)
                if not content:
                    break
                file_content += content
        print(file_content)
    except FileNotFoundError as err:
        print(f'{file_name} 未找到 {err}')
    else:
        print(f'{file_name} 读取完成')
    finally:
        print('最终处理逻辑')


def read_demo2():
    file_content = ''
    file_name = '文件.py'
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            limit = 1000
            while True:
                content = file.readline(limit)
                if not content:
                    break
                file_content += content
        print(file_content)
    except FileNotFoundError as err:
        print(f'{file_name} 未找到 {err}')
    else:
        print(f'{file_name} 读取完成')
    finally:
        print('最终处理逻辑')


def read_demo3():
    file_content = ''
    file_name = '文件.py'
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                file_content += line
        print(file_content)
    except FileNotFoundError as err:
        print(f'{file_name} 未找到 {err}')
    else:
        print(f'{file_name} 读取完成')
    finally:
        print('最终处理逻辑')


def read_demo4():
    file_content = ''
    file_name = '文件.py'
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            for line in file:
                file_content += line
        print(file_content)
    except FileNotFoundError as err:
        print(f'{file_name} 未找到 {err}')
    else:
        print(f'{file_name} 读取完成')
    finally:
        print('最终处理逻辑')


def write_demo1():
    file_name = 'xxx.txt'
    try:
        with open(file_name, mode='a', encoding='utf-8') as file:
            file.write('Hello World')
            file.writelines(['111\n', '222\n', '333\n'])
    except FileNotFoundError as err:
        print(f'{file_name} 未找到 {err}')
    else:
        print(f'{file_name} 写入完成')
    finally:
        print('最终处理逻辑')


def copy_file(src, dist):
    chunk = 1024 * 10
    try:
        with open(src, mode='rb') as old_file:
            try:
                with open(dist, mode='wb') as new_file:
                    while True:
                        content = old_file.read(chunk)
                        if not content:
                            break
                        new_file.write(content)
            except FileNotFoundError as err:
                print(f'{dist} 文件无法创建, {err}')
    except FileNotFoundError as err:
        print(f'{src} 文件不存在, {err}')


if __name__ == '__main__':
    old_file_name = r'C:\Users\zjw\Downloads\黑马python\python就业班\01 网络编程\02-udp\04-udp发送数据的强调.flv'
    new_file_name = r'C:\Users\zjw\Desktop\xxx.flv'
    copy_file(old_file_name, new_file_name)
