# coding=utf8
from multiprocessing import Pool
import os, time, random

def run_task(name):
    print 'Task %s (pid = %s) is running...' % (name, os.getpid())
    time.sleep(random.random() * 3)
    print 'Task %s end.' % name
    
if __name__ == '__main__':
    print 'Current process %s.' % os.getpid()
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close() # 调用join()之前先必须调用close()，调用close()之后就不会继续添加新的Process了
    p.join()
    print 'All subprocesses done.'

