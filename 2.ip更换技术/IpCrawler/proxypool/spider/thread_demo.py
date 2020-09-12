# -*- coding: utf-8 -*-

from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
import os
import time


#print("hi outside of main()")
def hello(x):
    print('inside hello()')
    print('Proccess id:', os.getpid())
    return x * x

def callback(res):
    print("进程池中的返回 " + res)
    return res

def fun():
    print('进城池中')
    return 'in'
if __name__ == '__main__':

    pool = Pool(processes=1)
    res = pool.apply_async(fun, callback=callback)
    print(res)
    print("祝进程中")
    #p = Pool(5)
    #p = ThreadPool(5)
    #pool_out = p.map(hello, range(3))
    #print(pool_out)
    #print(os.getpid())