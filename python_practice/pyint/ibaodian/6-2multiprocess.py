# -*- coding: UTF-8 -*-import multiprocessingdef fib(n,m_dict={}):    '''worker function'''    if n <= 1:        return 1    m_dict[i] = i    return fib(n-1) + fib(n-2)if __name__ == '__main__':    manager = multiprocessing.Manager()    return_dict = manager.dict()    jobs = []    for i in range(10,20):        p = multiprocessing.Process(target=fib,args=(i,return_dict))        jobs.append(p)        p.start()    for job in jobs:        job.join()    print(return_dict.items())