# coding=utf8
from multiprocessing import Pipe, Process
import random, time, os
from test.test_threading_local import target

'''
创建两个进程，一个通过Pipe发送数据，一个通过Pipe接收数据
'''
def proc_send(pipe, urls):
    for url in urls:
        print 'Process (%s) send: %s' % (os.getpid(), url)
        pipe.send(url)
        time.sleep(random.random())

def proc_recv(pipe):
    while True:
        print 'Process (%s) recv: %s' % (os.getpid(), pipe.recv())
        time.sleep(random.random())

if __name__ == '__main__':
    pipe = Pipe()
    p1 = Process(target=proc_send, args=(pipe[0], ['url_'+str(i) for i in range(10)]))
    p2 = Process(target=proc_recv, args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.terminate()
    
    
    
    