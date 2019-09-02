import socket

if __name__ == '__main__':
    bufferSize = 1024
    toClientData = "你好，我是 UDP 服务器端.".encode('utf-8')
    serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    serverSocket.bind(("127.0.0.1", 20001))
    print("UDP server up and listening")
    while True:
        fromClient = serverSocket.recvfrom(bufferSize)
        message = fromClient[0]
        address = fromClient[1]
        clientMsg = "Message from Client: {}".format(str(message, 'utf-8'))
        clientIP = "Client IP Address: {}".format(address)

        print(clientMsg)
        print(clientIP)

        serverSocket.sendto(toClientData, address)
