import socket


def sendMsg(udpSocket):
    '''
    send message function
    :param udpSocket:
    :return:
    '''
    message = input('Please Input What You Want To Send: ')
    destIp = input('Please input dest IP:')
    destPort = input('Please Input dest port: ')
    udpSocket.sendto(message.encode('utf-8'), (destIp, int(destPort)))


def recvMsg(udpSocket: socket):
    recvData = udpSocket.recvfrom(2048)
    print('%s %s' % (str(recvData[1]), recvData[0].decode('utf-8')))


def main():
    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpSocket.bind(('127.0.0.1', 7788))
    print('------ Listening At 127.0.0.1:7788 ------')

    print('0: exit')
    print('1: send message')
    print('2: receive message')
    while True:
        print('-----------------------------------------')
        option = input('Please input your action number: ')
        if option == '1':
            sendMsg(udpSocket)
        elif option == '2':
            recvMsg(udpSocket)
        elif option == '0':
            break
        else:
            print('Please input [0, 2, 3]!')


if __name__ == '__main__':
    main()
