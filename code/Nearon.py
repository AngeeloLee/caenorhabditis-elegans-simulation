#-*-coding:utf-8-*-
"""
基本神经元类及数据类定义
"""

#from abd import ABCMeta,abstractmethod
import threading
import datetime

#连接类型系数
linkTypeRatio = {
    'EJ': 1.0,
    'S': 1.0,
    'Sp': 1.0,
    'R': 1.0,
    'Rp': 1.0
}

class Signal:
    """
    用来传输信号的类，仅做数据结构体使用
    """
    def __init__(self,value=0,type=1,power=0):
        self.value = value  ##定义信号值
        self.type = type    ##定义信号类型
        self.power = power  ##定义信号强度

class Nearon:
    """
    用来保存某一神经元信息，用在某一神经元的前导神经元列表或后继神经元列表
    """
    def __init__(self,name='NONE', object=None, linkType='NONE',linkDistance=0,linkPower=0,signal=Signal()):
        self.name = name                    #定义神经元的名称属性
        self.object = object                #保存神经元对象的引用
        self.linkType = linkType            #定义连接类型
        self.linkDistance = linkDistance    #定义连接距离
        self.linkPower = linkPower          #定义连接强度，可能不需要，先写上之后再说吧
        self.signal = signal                #定义该神经要发送到该神经元或从该神经元上接受的信号

#------------------------------------------------------------------

class BaseNearon(threading.Thread):
    """
    神经元基类
    """
    def __init__(self,name='',font={},back={}):
        threading.Thread.__init__(self)
        self.name = name        #定义神经元名称
        self.fontNearon = font  #定义前导神经元字典列表，类型
        self.backNearon = back  #定义后继神经元字典列表，类型
        self.life = True
        self.event = False
        self.eventCaller = ''
    

    def run(self):
        while(self.life):
           if(self.event):
               self.Work()


    def stop(self):
        self.life = False


    def addNearon(self, position, nearon):
        if position == 'font':
            self.fontNearon[nearon.name] = nearon
        elif position == 'back':
            self.backNearon[nearon.name] = nearon


    def ReciveSignal(self,signal,senderNearonName):
        """接收信号方法
        signal:             信号对象
        senderNearonName:   发送者神经元的名字，用于查找对应神经元
        """
        self.fontNearon[senderNearonName].signal.value = signal.value
        self.fontNearon[senderNearonName].signal.type = signal.type
        self.fontNearon[senderNearonName].signal.power = signal.power

        #发起一个事件
        self.event = True
        self.eventCaller = senderNearonName
        

    def SendSignal(self,targetNearonName):
        """发送信号方法
        targetNearonName:   目标神经元名字，用于查找对应神经元
        """
        self.backNearon[targetNearonName].object.ReciveSignal(self.backNearon[targetNearonName].signal,self.name)


    def MakeSignal(self):
        """信号处理方法
        """
        resivedSignalValue = self.fontNearon[self.eventCaller].signal.value
        resivedSignalType = self.fontNearon[self.eventCaller].signal.type
        resivedSignalPower = self.fontNearon[self.eventCaller].signal.power
        targetSignalValue = resivedSignalValue*resivedSignalPower
        for name,nearon in self.backNearon.items():
            targetSignalValue *= linkTypeRatio[nearon.linkType]
            targetSignalValue = 0-targetSignalValue if self.fontNearon[self.eventCaller].signal.type == -1 else targetSignalValue
            nearon.signal.value += targetSignalValue * (1 + 1/nearon.linkDistance)


    def log(self, action, targetOrOrignalNearonName):
        """日志记录方法 
        """
        logFile = open(self.name+'-log.txt', 'a')
        logInfo = datetime.datetime.now().strftime() + ' => [' + self.name + '] '
        if action == 'send':
            logInfo += 'send to [' + targetOrOrignalNearonName + '] a Signal with '
            logInfo += 'Value=' + self.backNearon[targetOrOrignalNearonName].Signal.Value
            logInfo += ' Power=' + self.backNearon[targetOrOrignalNearonName].Signal.power
            logInfo += ' Type=' + self.backNearon[targetOrOrignalNearonName].Signal.type
            logFile.write(logInfo)
        elif action == 'recive':
            logInfo += 'resive from [' + targetOrOrignalNearonName + '] a Signal with '
            logInfo += 'Value=' + self.fontNearon[targetOrOrignalNearonName].Signal.Value
            logInfo += ' Power=' + self.fontNearon[targetOrOrignalNearonName].Signal.power
            logInfo += ' Type=' + self.fontNearon[targetOrOrignalNearonName].Signal.type
            logFile.write(logInfo)


    def Work(self):
        """神经元工作方法，接收到信号后调用该方法
        """
        pass

#-------------------------------------------------------------


class SansorNearon(BaseNearon):
    """感觉神经元
    """
    pass