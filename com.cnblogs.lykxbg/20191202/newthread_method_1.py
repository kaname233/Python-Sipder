# coding=utf8
"""
创建多线程的方式一：
    把函数传入并创建Thread实例，然后调用start方法开始执行
"""
import random, time
import threading

def thread_run(urls):
    print 'Current thread %s is running...' % threading.current_thread().name
    for url in urls:
        print '%s -->>> %s' % (threading.current_thread().name, url)
        time.sleep(random.random())
    print '%s ended.' % threading.current_thread().name

if __name__ == '__main__':
    print 'Current thread %s is running...' % threading.current_thread().name
    t1 = threading.Thread(target=thread_run, name='Thread_1', args=(['url_1','url_2','url_3'],))
    t2 = threading.Thread(target=thread_run, name='Thread_2', args=(['url_4','url_5','url_6'],))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print '%s ended.' % threading.current_thread().name
