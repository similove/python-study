import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.bind(('', 17788))
tcpSocket.listen(128)
print('------ Listening At 127.0.0.1:17788 ------')

while True:
    clientSocket, clientAddr = tcpSocket.accept()
    recvData = clientSocket.recv(4096)
    print('接收到客户端数据', recvData.decode('utf-8'))
    fileContent = open('TCPServer.py', 'r').read(4096)
    clientSocket.send(fileContent.encode('utf-8'))
    clientSocket.close()
