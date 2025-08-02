class processor():
    # atribut
    __name = "blank"
    __price = 0

    # constructor
    def __init__(self):
        self.__name = "blank"
        self.__price = 0

        
    def __init__(self, name="blank", price=0):
        self.__name = name;
        self.__price = price;

    # setter dan getter

    def setName(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name 

    def setPrice(self, price):
        self.__price = price
        
    def getPrice(self):
        return self.__price 