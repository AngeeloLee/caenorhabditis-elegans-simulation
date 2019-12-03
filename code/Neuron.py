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

class Neuron:
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

class BaseNeuron(threading.Thread):
    """
    神经元基类
    """
    def __init__(self,name='',font={},back={}):
        threading.Thread.__init__(self)
        self.name = name        #定义神经元名称
        self.fontNeuron = font  #定义前导神经元字典列表，类型
        self.backNeuron = back  #定义后继神经元字典列表，类型
        self.life = True
        self.event = False
        self.eventCaller = ''
    

    def run(self):
        while(self.life):
           if(self.event):
               self.Work()


    def stop(self):
        self.life = False


    def addNeuron(self, position, Neuron):
        if position == 'font':
            self.fontNeuron[Neuron.name] = Neuron
        elif position == 'back':
            self.backNeuron[Neuron.name] = Neuron


    def ReciveSignal(self,signal,senderNeuronName):
        """接收信号方法
        signal:             信号对象
        senderNeuronName:   发送者神经元的名字，用于查找对应神经元
        """
        self.fontNeuron[senderNeuronName].signal.value = signal.value
        self.fontNeuron[senderNeuronName].signal.type = signal.type
        self.fontNeuron[senderNeuronName].signal.power = signal.power

        #发起一个事件
        self.event = True
        self.eventCaller = senderNeuronName
        

    def SendSignal(self,targetNeuronName):
        """发送信号方法
        targetNeuronName:   目标神经元名字，用于查找对应神经元
        """
        self.backNeuron[targetNeuronName].object.ReciveSignal(self.backNeuron[targetNeuronName].signal,self.name)


    def MakeSignal(self):
        """信号处理方法
        """
        resivedSignalValue = self.fontNeuron[self.eventCaller].signal.value
        resivedSignalType = self.fontNeuron[self.eventCaller].signal.type
        resivedSignalPower = self.fontNeuron[self.eventCaller].signal.power
        targetSignalValue = resivedSignalValue*resivedSignalPower
        for name,Neuron in self.backNeuron.items():
            targetSignalValue *= linkTypeRatio[Neuron.linkType]
            targetSignalValue = 0-targetSignalValue if self.fontNeuron[self.eventCaller].signal.type == -1 else targetSignalValue
            Neuron.signal.value += targetSignalValue * (1 + 1/Neuron.linkDistance)


    def log(self, action, targetOrOrignalNeuronName):
        """日志记录方法 
        """
        logFile = open(self.name+'-log.txt', 'a')
        logInfo = datetime.datetime.now().strftime() + ' => [' + self.name + '] '
        if action == 'send':
            logInfo += 'send to [' + targetOrOrignalNeuronName + '] a Signal with '
            logInfo += 'Value=' + self.backNeuron[targetOrOrignalNeuronName].Signal.Value
            logInfo += ' Power=' + self.backNeuron[targetOrOrignalNeuronName].Signal.power
            logInfo += ' Type=' + self.backNeuron[targetOrOrignalNeuronName].Signal.type
            logFile.write(logInfo)
        elif action == 'recive':
            logInfo += 'resive from [' + targetOrOrignalNeuronName + '] a Signal with '
            logInfo += 'Value=' + self.fontNeuron[targetOrOrignalNeuronName].Signal.Value
            logInfo += ' Power=' + self.fontNeuron[targetOrOrignalNeuronName].Signal.power
            logInfo += ' Type=' + self.fontNeuron[targetOrOrignalNeuronName].Signal.type
            logFile.write(logInfo)


    def Work(self):
        """神经元工作方法，接收到信号后调用该方法
        """
        pass

#-------------------------------------------------------------


class SansorNeuron(BaseNeuron):
    """感觉神经元
    """
    pass