from socket import *

tcpSocket = socket(AF_INET, SOCK_STREAM)
serverIp = input('服务器IP: ')
serverPort = input('服务器端口: ')
tcpSocket.connect((serverIp, int(serverPort)))
sendData = input('请输入数据: ')
tcpSocket.send(sendData.encode('utf-8'))
recvData = tcpSocket.recv(4096)
print('接收到服务器端回复数据: ', recvData.decode('utf-8'))
tcpSocket.close()
