import socket
import threading
import re

# author zjw <cn.zjwblog@gmail.com>
# date 2019/9/4 下午8:51
base = '../html'


def recv_and_send_msg(client_socket, client_address):
    '''
    处理单个请求.
    :param client_socket:
    :param client_address:
    :return:
    '''
    request_data = client_socket.recv(4096)
    text = request_data.decode('utf-8')
    print('接收到客户[%s]端数据:\n%s' % (str(client_address), text), '-' * 50)

    try:
        request_lines = text.splitlines()
        ret = re.match(r'[^/]*(/[^ ]*)', request_lines[0])
        file_name = ''
        if ret:
            file_name = ret.group(1)
            if file_name == '/':
                file_name = '/index.html'
        file = open(base + file_name, 'rb')
        content = file.read()
        file.close()
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html; charset=utf-8\r\n"
        response += "\r\n"

        client_socket.send(response.encode('utf-8'))
        client_socket.send(content)
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "Content-Type: text/html; charset=utf-8\r\n"
        response += "\r\n"
        response += 'File Not Found!'
        client_socket.send(response.encode('utf-8'))
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 12345))
    server_socket.listen(128)
    print('------ Listening At 127.0.0.1:12345 ------')
    while True:
        client = server_socket.accept()
        threading.Thread(target=recv_and_send_msg, args=client).start()


if __name__ == '__main__':
    main()
