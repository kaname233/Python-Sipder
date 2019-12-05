# coding=utf8
"""
1. 创建Socket，绑定Socket到本地IP和端口
2. 开始监听连接
3. 进入循环，不断接收客户端的连接请求
4. 接收传来的数据，并发送给对方数据
5. 传输完毕后，关闭Socket
"""
import socket
import threading
import time


def dealClient(sock, addr):
    # 4. 接收传来的数据，并发送给对方数据
    print 'Accept new connection from %s:%s...' % addr
    sock.send(b'Hello, I am server!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print '-->>%s!' % data.decode('utf-8')
        sock.send('Loop_Msg: %s!' % data.decode('utf-8').encode('utf-8'))
    # 5. 传输完毕后，关闭Socket
    sock.close()
    print 'Connection from %s:%s closed.' % addr

if __name__ == '__main__':
    # 1. 创建Socket，绑定Socket到本地IP和端口
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1',9999))
    # 2. 开始监听连接
    s.listen(5) # listen(n)传入的值, n表示的是服务器拒绝(超过限制数量的)连接之前，操作系统可以挂起的最大连接数量。n也可以看作是"排队的数量"
    print 'Waiting for connection...'
    # 3. 进入循环，不断接收客户端的连接请求
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=dealClient, args=(sock, addr))
        t.start()