import socket
import threading


# author zjw <cn.zjwblog@gmail.com>
# date 2019/9/4 下午8:51


def recv_and_send_msg(client_socket, client_address):
    while True:
        request_data = client_socket.recv(4096)
        text = request_data.decode('utf-8')
        print('接收到客户[%s]端数据: %s' % (str(client_address), text))
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html; charset=utf-8\r\n"
        response += "\r\n"
        response += "<h1>我是服务器端.<h1>"
        client_socket.send(response.encode("utf-8"))
        client_socket.close()


def accept_conn(client_socket, client_address):
    threading.Thread(target=recv_and_send_msg,
                     args=(client_socket, client_address)).start()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 16789))
    server_socket.listen(128)
    print('------ Listening At 127.0.0.1:16789 ------')
    while True:
        client = server_socket.accept()
        threading.Thread(target=accept_conn, args=client).start()


if __name__ == '__main__':
    main()
