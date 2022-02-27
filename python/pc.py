from processor import processor
from disk import disk
from ram import ram

class pc():
    # atribut
    __pObj = processor()
    __dObj = disk()
    __rObj = ram()
    __totalPrice = 0

    # constructor
    def __init__(self):
        self.__pObj = processor()
        self.__dObj = disk()
        self.__rObj = ram()
        self.__totalPrice = 0
    
    def __init__(self, pObj = processor, dObj = disk, rObj = ram):
        self.__pObj = pObj
        self.__dObj = dObj
        self.__rObj = rObj

    # setter dan getter
    def setpObj(self, pObj):
        self.__pObj = pObj
        
    def getpObj(self):
        return self.__pObj 

    def setdObj(self, dObj):
        self.__dObj = dObj
        
    def getdObj(self):
        return self.__dObj 

    def setrObj(self, rObj):
        self.__rObj = rObj
        
    def getrObj(self):
        return self.__rObj 

    def setTotalPrice(self, totalPrice):
        self.__totalPrice = totalPrice
        
    def getTotalPrice(self):
        # self.__totalPrice =  self.pObj.getPrice() + self.dObj.getPrice() + self.rObj.getPrice()
        return self.__totalPrice
        # return self.__totalPrice 