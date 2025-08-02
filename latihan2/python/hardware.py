from product import product

class hardware(product):
    # atribut
    __brand = "blank"
    __model = "blank"

    # constructor
    def __init__(self, model="blank", brand="blank"):
        self.__brand = brand
        self.__model = model

    # Setter dan Getter

    def setBrand(self, brand):
        self.__brand = brand
        
    def getBrand(self):
        return self.__brand 

    def setModel(self, model):
        self.__model = model
        
    def getModel(self):
        return self.__model 
