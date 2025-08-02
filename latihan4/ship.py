from vehicle import vehicle

class ship(vehicle):
    # atribut
    __age = 0
    __countryOfManufacture = ";"

    # constructor
    def __init__(self):
        super().__init__()
        self.__age = 0
        self.__countryOfManufacture = ";"    

    # atribut biasa
    def setShip(self, fuelType, maxPassengers, age, countryOfManufacture):
        self.setVehicle(fuelType, maxPassengers)
        self.__age = age
        self.__countryOfManufacture = countryOfManufacture

    # atribut objek
    def setKapal(self, swim):
        self.setKendaraan(swim)
        self.__age = swim.__age
        self.__countryOfManufacture = swim.__countryOfManufacture
        
    # setter dan getter

    def setAge(self, age):
        self.__age = age
        
    def getAge(self):
        return self.__age 

    def setCountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture
        
    def getCountryOfManufacture(self):
        return self.__countryOfManufacture 

    # output
    def showShip(self):
        self.move()
        print("Umur kapal : ", (self.getAge()))
        print("Negara pembuat : ", (self.getCountryOfManufacture()))