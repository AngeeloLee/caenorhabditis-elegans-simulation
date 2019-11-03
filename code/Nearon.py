#-*-coding:utf-8-*-
"""
基本神经元类及数据类定义
"""

from abd import ABCMeta,abstractmethod

class Signal:
    """"
    用来传输信号的类，仅做数据结构体使用
    """
    def __init__(self,value=0,type='NONE',power=0):
        self.value = value  ##定义信号值
        self.type = type    ##定义信号类型
        self.power = power  ##定义信号强度

class Nearon:
    """
    用来保存某一神经元信息，用在某一神经元的前导神经元列表或后继神经元列表
    """
    def __init__(self,name='NONE',linkType='NONE',linkDistance=0,linkPower=0,signal=Signal()):
        self.name = name                    #定义神经元的名称属性
        self.linkType = linkType            #定义连接类型
        self.linkDistance = linkDistance    #定义连接距离
        self.linkPower = linkPower          #定义连接强度，可能不需要，先写上之后再说吧
        self.signal = signal                #定义该神经要发送到该神经元或从该神经元上接受的信号

#------------------------------------------------------------------

class BaseNearon:
    """
    神经元基类
    """
    def __init__(self,name='',font=[],back=[]):
        self.name = name        #定义神经元名称
        self.fontNearon = font  #定义前导神经元列表
        self.backNearon = back  #定义后继神经元列表

    def ReciveSignal(self,signal,senderNearonName):
        """接收信号函数
        signal:             信号对象
        senderNearonName:   发送者神经元的名字，用于查找对应神经元
        """
        for nearon in self.fontNearon:#####寻找发送者神经元
            if nearon.name == senderNearonName:     #对比神经元名字
                nearon.signal.value = signal.value  # ┐
                nearon.signal.type = signal.type    # ├ 若找到的话赋值
                nearon.signal.power = signal.power  # ┘
                break

    def SendSignal(self,targetNearonObject,targetNearonName):
        """发送信号函数
        targetNearonObject: 目标神经元对象，类型为BaseNearon
        targetNearonName:   目标神经元名字，用于查找对应神经元
        """
        for nearon in self.backNearon:####寻找需要发送给目标神经元的信号
            if nearon.name == targetNearonName:     #对比神经元名字
                targetNearonObject.ReciveSignal(nearon.signal,self.name)    #调用目标神经元对象的接收函数实现
                break

    def MakeSignal():
        """信号处理函数，虚函数
        """
        pass