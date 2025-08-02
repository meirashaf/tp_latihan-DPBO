from vehicle import vehicle

class airplane(vehicle):
    # atribut
    __age = 0
    __wingsLength = 0

    # constructor
    def __init__(self):
        super().__init__()
        self.__age = 0
        self.__wingsLength = 0

    # atribut biasa
    def setAirplane(self, fuelType=".", maxPassengers=0, age=0, wingsLength=0):
        self.setVehicle(fuelType, maxPassengers)
        self.__age = age
        self.__wingsLength = wingsLength

    # atribut objek
    def setPesawat(self, fly):
        self.setKendaraan(fly)
        self.__age = fly.__age
        self.__wingsLength = fly.__wingsLength
        
    # setter dan getter

    def setAge(self, age):
        self.__age = age
        
    def getAge(self):
        return self.__age 
           
    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength
        
    def getWingsLength(self):
        return self.__wingsLength 
   
    # output
    def showAirplane(self):
        self.move()
        print("Umur pesawat : ", (self.getAge()))
        print("Lebar sayap : ", (self.getWingsLength()))
    