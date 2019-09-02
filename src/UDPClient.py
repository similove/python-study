import socket

if __name__ == '__main__':
    bufSize = 1024
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    destIpAndPort = input('请输入对方服务器IP和端口，以空格分隔: ')
    toServer = input('请输入要发送的内容: ')

    ipAndPort = destIpAndPort.split(':')

    toServerData = toServer.encode('utf-8')
    client.sendto(toServerData, (ipAndPort[0], int(ipAndPort[1])))
    fromServer = client.recvfrom(bufSize)
    message = fromServer[0]
    address = fromServer[1]

    msg = "Message from Server: {}".format(str(message, 'utf-8'))
    serverAddress = "Server IP Address: {}".format(address)
    print(msg)
    print(serverAddress)
