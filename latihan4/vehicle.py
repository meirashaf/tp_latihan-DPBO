
class vehicle():
    # atribut
    __fuelType = "."
    __maxPassengers = 0
    
    # constructor
    def __init__(self):
        self.__fuelType = "."
        self.__maxPassengers = 0

    # atribut biasa
    def setVehicle(self, fuelType, maxPassengers):
        self.__fuelType = fuelType
        self.__maxPassengers = maxPassengers

    # atribut objek
    def setKendaraan(self, angkot):
        self.__fuelType = angkot.__fuelType
        self.__maxPassengers = angkot.__maxPassengers

    # setter dan getter

    def setFuelType(self, fuelType):
        self.__fuelType = fuelType
        
    def getFuelType(self):
        return self.__fuelType 

    def setMaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers
        
    def getMaxPassengers(self):
        return self.__maxPassengers 

    # output
    def move(self):
        print("Tipe bahan bakar : ", (self.getFuelType()))
        print("Jumlah maksimum penumpang : ", (self.getMaxPassengers()))