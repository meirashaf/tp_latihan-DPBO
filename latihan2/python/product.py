class product():
    # atribut
    __price = 0
    __idProduct = "blank"

    # constructor
    def __init__(self, price=0, idProduct="blank"):
        self.__price = price
        self.__idProduct = idProduct

    # Setter dan Getter

    def setPrice(self, price):
        self.__price = price
        
    def getPrice(self):
        return self.__price 

    def setIdProduct(self, idProduct):
        self.__idProduct = idProduct
        
    def getIdProduct(self):
        return self.__idProduct 
