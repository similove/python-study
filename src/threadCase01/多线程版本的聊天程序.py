import socket
import threading


def recv_msg(client_socket, client_address):
    while True:
        recv_data = client_socket.recv(4096)
        text = recv_data.decode('utf-8')
        if text == 'exit':
            print('客户端退出...')
            break
        print('接收到客户[%s]端数据: %s' % (str(client_address), text))


def send_msg(client_socket, client_address):
    while True:
        text = input('请输入[%s]: ' % str(client_address,))
        if text == 'exit':
            print('服务器端退出...')
            break
        client_socket.send((text + '\n').encode('utf-8'))


def accept_conn(client_socket, client_address):
    threading.Thread(target=recv_msg, args=(client_socket, client_address)).start()
    threading.Thread(target=send_msg, args=(client_socket, client_address)).start()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 17788))
    server_socket.listen(128)
    print('------ Listening At 127.0.0.1:17788 ------')
    while True:
        client = server_socket.accept()
        threading.Thread(target=accept_conn, args=client).start()


if __name__ == '__main__':
    main()
