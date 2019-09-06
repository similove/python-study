# coding: utf-8
import socket
# import time


# author zjw <cn.zjwblog@gmail.com>
# date 2019/9/5 上午11:13


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(('', 1234))
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)

    client_socket_list = list()

    while True:
        # time.sleep(0.5)
        try:
            new_socket, new_addr = tcp_server_socket.accept()
        except:
            # print('# No Client Connection...')
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(4096)
            except:
                # print('# Client Not Send Message.')
                pass
            else:
                if recv_data:
                    print(recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)
                    # print('# Client Closed.')


if __name__ == '__main__':
    main()
