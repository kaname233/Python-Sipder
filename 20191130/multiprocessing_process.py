# coding=utf8
import os
from multiprocessing import Process
def run_proc(name):
    print 'child process %s (%s) running...' %(name, os.getpid())
if __name__ == '__main__':
    print 'Parent process is %s.' % os.getpid()
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print 'process will start'
        p.start()
    p.join()
    print 'main process end'
        
    
    