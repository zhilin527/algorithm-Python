# -*- coding: UTF-8 -*-import time# observer,listener,hook,callback都是观察者# 事件类 fire Eventclass wakeUpEvent():    def __init__(self,timestamp,loc,source):        self.timestamp = timestamp        self.loc = loc        self.source =source# 观察者class observer():    def actionsOnWakeUp(self):        passclass Dad(observer):    def actionsOnWakeUp(self,event):        print('Child is crying?: ')        print(event.source.isCry())        print('time:'+ event.timestamp + ',loc: '+event.loc +',come from '+str(event.source)+ ', ->Dad Feeding...')class Mom(observer):    def actionsOnWakeUp(self,event):        print('Child is crying?: ')        print(event.source.isCry())        print('time: '+ event.timestamp + ',loc : '+event.loc + ',come from '+str(event.source)+', -> Mon Huging...')class Dog(observer):    def actionsOnWakeUp(self,event):        print('Child is crying?: ')        print(event.source.isCry())        print('time: '+ event.timestamp + ',loc : '+event.loc + ',come from '+str(event.source)+', -> Dog wang...')# 被观察者class Child():    def __init__(self):        self.cry = False        self.observers = [Dad(),Mom(),Dog()]    def isCry(self):        return self.cry    def wakeUp(self):        self.cry = True        event = wakeUpEvent(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),'bed',self)        for ob in self.observers:            ob.actionsOnWakeUp(event)c = Child()c.wakeUp()