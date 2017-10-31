# import os
# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# from multiprocessing import Process
# import os

# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

#多进程
# from multiprocessing import Pool
# import os,time,random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end =  time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

#子进程

# import subprocess

# print('$ nslookup www.python.org')
# #这是一个可以执行命令行语句的子进程
# r = subprocess.call(['ls'])
# print('Exit code:', r)

# import subprocess

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)


# #进程间通信
# from multiprocessing import Process,Queue
# import os,time,random
# #写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ["A","B","C"]:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())

# # 读数据进程执行的代码:
# def read(q):
#     print ('Process to read: %s ' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
# if __name__ == '__main__':
#     # 父进程创建Queue,并传给各个子进程:
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()

#多线程

#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
# import time, threading

# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)
# Lock锁
'''
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，
互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
'''

# import time ,threading
# #假定这是你的银行存款
# balance = 0
# lock = threading.Lock()

# def change_it(n):
#     #先存后取,结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n 

# def run_thread(n):

#     for i in range(10000000):
#         #先要获取锁
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             #改完了一定要释放所:
#             lock.release()

# t1 = threading.Thread(target=run_thread,args=(5,))
# t2 = threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)


#ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事：
# import threading
# local_school = threading.local()
# def process_student():
#     # 获取当前线程关联的student：
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))
# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()

# t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
# t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#分布式进程



