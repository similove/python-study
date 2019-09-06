# coding: utf-8
import socket
import re
import time


# author zjw <cn.zjwblog@gmail.com>
# date 2019/9/5 上午11:13


base = '../html'


def get_file_content(filename):
    with open(filename, 'rb') as file:
        content = file.read()
        return content


def request_handler(recv_data, client_socket):
    '''
    处理单个请求.
    :param client_socket:
    :return:
    '''
    text = recv_data.decode('utf-8')
    # print('接收到客户端数据:\n%s' % text, '-' * 50)

    try:
        request_lines = text.splitlines()
        ret = re.match(r'[^/]*(/[^ ]*)', request_lines[0])
        file_name = ''
        if ret:
            file_name = ret.group(1)
            if file_name == '/':
                file_name = '/index.html'

        response_body = get_file_content(base + file_name)

        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Type: text/html; charset=utf-8\r\n"
        response_header += 'Content-Length:%d\r\n' % len(response_body)
        response_header += "\r\n"

        client_socket.send(response_header.encode('utf-8') + response_body)

    except:
        response_body = 'File Not Found!'
        response_header = "HTTP/1.1 404 NOT FOUND\r\n"
        response_header += 'Content-Length:%d\r\n' % len(response_body)
        response_header += "Content-Type: text/html; charset=utf-8\r\n"
        response_header += "\r\n"

        client_socket.send(response_header.encode('utf-8') + response_body.encode('utf-8'))
    client_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(('', 1234))
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)

    client_socket_list = list()

    while True:
        time.sleep(0.5)
        try:
            new_socket, new_addr = tcp_server_socket.accept()
        except:
            print('# No Client Connection...')
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(4096)
            except:
                print('# Client Not Send Message.')
                pass
            else:
                if recv_data:
                    # 处理请求
                    request_handler(recv_data, client_socket)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)
                    print('# Client Closed.')


if __name__ == '__main__':
    main()
