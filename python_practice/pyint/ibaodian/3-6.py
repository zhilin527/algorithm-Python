#什么事生成器#1。生成器就是可以生成值的函数#2。当一个函数里有了yield关键字就成了生成器#3。生成器可以挂起执行并且保持当前执行的状态def simple_gen():    yield 'hello'    yield 'world'gen = simple_gen()print(type(gen))print(next(gen))print(next(gen))#基于生成器的协程def coro():    hello = yield 'hello'    yield helloc = coro()#输出'hello'，这里调用next产出第一个值'hello'，之后函数暂停print(next(c))#再次调用send发送值，此时hello变量赋值为'world'，然后产出hello变量的值'world'print(c.send('world'))#之后协程结束，后续在send会抛出异常StopIteration##协程需要注意的地方，#1。协程需要使用send(None)或者next(corotine)来预激才能启动#2。在yield处协程会暂停#3。单独的yield value会产出值给调用方#4。可以通过corotine.send(value)给协程发送值，发送的值会赋值给yield表达式左边的变量#5。协程执行完，没有遇到写一个yield语句，会抛出StopIteration异常#python3原生协程#引入async/await支持原生协程import asyncioimport datetimeimport randomasync def display_date(num,loop):    end_time = loop.time() + 50.0    while True:        print('Loop: {} Time: {}'.format(num,datetime.datetime.now()))        if (loop.time() + 1.0) >= end_time:            break        await asyncio.sleep(random.randint(0,5))loop = asyncio.get_event_loop()asyncio.ensure_future(display_date(1,loop))asyncio.ensure_future(display_date(2,loop))loop.run_forever()