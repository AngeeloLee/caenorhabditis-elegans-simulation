# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:34:50 2019

@author: asus
"""
from abd import ABCMeta,abstractmethod ##映入虚函数包
Sign = { ##定义一个信号字典
    fontNearon:'',
    backNearon:'',
    reciverSign:'',
    reciverSignType:'',
    reciverSignPower:'',
    sendSign:'',
    sendSignType:'',
    sendSignTypePower:'',
    nearonType:''}
class BaseNearon:
    __metaClass__ = ABCMeta ##先声明虚函数 　　　
    __fontNearon = []
    __backNearon = []
    __reciverSign = []
    __reciverSignType = []
    __reciverSignPower = []
    __sendSign = []
    __sendSignType = []
    __sendSignTypePower = []
    __nearonType = ''
    def __init__(self,fontNearon,backNearon,reciverSign,reciverSignType,reciverSignPower,sendSign,sendSignType,sendSignTypePower,nearonType):
        self.__fontNearon = fontNearon
        self.__backNearon = backNearon
        self.__reciverSign = reciverSign
        self.__reciverSignType = reciverSignType
        self.__reciverSignPower = reciverSignPower
        self.__sendSign = sendSign
        self.__sendSignType = sendSignType
        self.__sendSignTypePower = sendSignTypePower
        self.__nearonType = nearonType
    def ReciverSign(destinateNeron,sign): ##暂时没写
        pass ##do nothing保持结构完整
        
    def SendSign(destinateNeron,sign): ##暂时没写
        pass ##do nothing
    @abstractmethod ##虚函数
    def MakeSign():
        pass

class SensorNearon(BaseNearon): ##感觉神经元
    __sensorCall = []
    __sensorSign = []
    def ScanSensor():
        pass        

class MotorNearon(BaseNearon):##运动神经元
    __motorCall = []
    __motorSign = []
    def MakeAction():
        pass
    
class InterNearon(BaseNearon):##中间神经元
    def TransSign():
        pass
    def CopySign():
        pass
    
 class NonNearonCell: ##非神经元细胞
     __connectNearon = []
     __sign = []
     __signType = []
     __signPower = []
     __cellType = []
     def SendSign():
         pass
     def ReciverSign():
         pass
     def MakeAction():
         pass
     
     