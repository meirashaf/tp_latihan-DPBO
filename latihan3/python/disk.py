class disk():
    # atribut
    __type = "blank"
    __capacity = 0
    __price = 0

    # constructor
    def __init__(self):
        self.__type = "blank"
        self.__capacity = 0
        self.__price = 0
        
        
    def __init__(self, type="blank", capacity=0, price=0):
        self.__type = type;
        self.__capacity = capacity;
        self.__price = price;

    # setter dan getter
    def setType(self, type):
        self.__type = type
        
    def getType(self):
        return self.__type 

    def setCapacity(self, capacity):
        self.__capacity = capacity
        
    def getCapacity(self):
        return self.__capacity 

    def setPrice(self, price):
        self.__price = price
        
    def getPrice(self):
        return self.__price 