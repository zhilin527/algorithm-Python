# -*- coding: UTF-8 -*-from collections import Iterable,Iterator# 可变对象，不可变对象# list set dict# int float tuple# 修改不可变类型内部的值，其内存地址id会变化# 修改可变类型内部的值，其内存地址id不会变化# python函数参数传递都是引用传递，传递一个arr进去，函数可以修改arr# 浅拷贝，深拷贝，# 浅拷贝只拷贝外层对象，内层嵌套的不拷贝，因此对外层的修改不影响，对内层的修改会导致拷贝对象也修改了# 深拷贝外层对象，和内层对象都拷贝，因此不管怎么修改都不影响# 赋值=，在同一片内存区域多了一个引用，修改原对象回变化# a = [1, 2, 3, 4, ['a', 'b']] #原始对象# b = a                       #赋值，传对象的引用# c = copy.copy(a)            #对象拷贝，浅拷贝# d = copy.deepcopy(a)        #对象拷贝，深拷贝# a.append(5)                 #修改对象a# a[4].append('c')            #修改对象a中的['a', 'b']数组子对象# b会全变，因为只是多了个引用# c外层不会变，因为拷贝了外层；内层嵌套的会变，因为没有拷贝# d都不会变，因为都拷贝了class A(Iterator):    pass# class Iterable(metaclass=ABCMeta):##     __slots__ = ()##     @abstractmethod#     def __iter__(self):#         while False:#             yield None##     @classmethod#     def __subclasshook__(cls, C):#         if cls is Iterable:#             return _check_methods(C, "__iter__")#         return NotImplemented### class Iterator(Iterable):##     __slots__ = ()##     @abstractmethod#     def __next__(self):#         'Return the next item from the iterator. When exhausted, raise StopIteration'#         raise StopIteration##     def __iter__(self):#         return self##     @classmethod#     def __subclasshook__(cls, C):#         if cls is Iterator:#             return _check_methods(C, '__iter__', '__next__')#         return NotImplemented