# coding=utf8
"""
1. 创建Socket，连接远端地址
2. 连接后发送数据和接收数据
3. 传输完毕后，关闭Socket
"""
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print '-->>'+s.recv(1024).decode('utf-8')
s.send(b'Hello I am a client')
print '-->>'+s.recv(1024).decode('utf-8')
s.send(b'exit')
s.close()