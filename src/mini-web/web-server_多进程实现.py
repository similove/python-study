# coding: utf-8
import socket
import multiprocessing
import re

# @author zjw<cn.zjwblog@gmail.com>
# @date 2019/9/6 上午08:13


base = '../../html'


def service_client(client_socket):
    '''
    处理单个请求.
    :param client_socket:
    :return:
    '''
    request_data = client_socket.recv(4096).decode('utf-8')
    print('接收到客户端数据:\n%s' % request_data, '-' * 50)

    request_lines = request_data.splitlines()

    file_name = ''

    ret = re.match(r'[^/]*(/[^ ]*)', request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == '/':
            file_name = '/index.html'

    try:
        file = open(base + file_name, 'rb')
    except:
        content = 'File Not Found!'.encode('utf-8')

        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "Content-Type: text/html; charset=utf-8\r\n"
        response += 'Content-Length:%d\r\n' % len(content)
        response += "\r\n"

        client_socket.send(response.encode('utf-8'))
        client_socket.send(content)
    else:
        content = file.read()
        file.close()

        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html; charset=utf-8\r\n"
        response += 'Content-Length:%d\r\n' % len(content)
        response += "\r\n"

        client_socket.send(response.encode('utf-8'))
        client_socket.send(content)

    client_socket.close()


def main():
    # 创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口
    server_socket.bind(('', 12345))
    # 设置为监听套接字
    server_socket.listen(128)
    print('------ Listening At 127.0.0.1:12345 ------')
    while True:
        client_socket, client_addr = server_socket.accept()
        multiprocessing.Process(target=service_client, args=(client_socket,)).start()
        client_socket.close()


if __name__ == '__main__':
    main()
