# coding=utf8
'''
从父进程创建三个子进程，两个进程往Queue中写数据，一个从Queue中读数据
'''
from multiprocessing import Process, Queue
import os, time, random
from test.test_threading_local import target

# 写进程
def proc_write(q,urls):
    print 'Process (%s) is writing...' % os.getpid()
    for url in urls:
        q.put(url)
        print 'Put %s to Queue...' % url
        time.sleep(random.random())

# 读进程
def proc_read(q):
    print 'Process %s is reading...' % os.getpid()
    while True:
        url = q.get()
        print 'Get %s from queue' % url
        
if __name__ == '__main__':
    q = Queue()
    writer1 = Process(target=proc_write, args=(q, ['url_1','url_2','url_3']))
    writer2 = Process(target=proc_write, args=(q, ['url_4','url_5','url_6']))
    reader = Process(target=proc_read, args=(q,))
    # 启动写进程
    writer1.start()
    writer2.start()
    # 启动读进程
    reader.start()
    # 等待写进程结束
    writer1.join()
    writer2.join()
    # 强制结束读进程
    reader.terminate()
    
    
    
    
    
    
    
    
    
    
    