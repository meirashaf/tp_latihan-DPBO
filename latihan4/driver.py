# : lisenceID, activeUntil, vehicleType
from ship import ship
from airplane import airplane

class driver(ship, airplane):
    # atribut
    __licenseID = 0
    __activeUntil = ";"
    __vehicleType = ";"

    # constructor
    def __init__(self):
        self.__licenseID = 0
        self.__activeUntil = ";"
        self.__vehicleType = ";"

    # secara atribut parameter biasa
    def setDriver(self, licenseID, activeUntil, vehicleType):
        self.__licenseID = licenseID
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType

    # secara atribut objek
    def setSupir(self, supir):
        self.__licenseID = supir.__licenseID
        self.__activeUntil = supir.__activeUntil
        self.__vehicleType = supir.__vehicleType
    
    # setter dan getter

    def setLicenseID(self, licenseID):
        self.__licenseID = licenseID
        
    def getLicenseID(self):
        return self.__licenseID 
    
    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil
        
    def getActiveUntil(self):
        return self.__activeUntil 
    
    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType
        
    def getVehicleType(self):
        return self.__vehicleType 
    
    # output
    def showDriver(self, swim, fly):
        print("License ID : ", (self.getLicenseID()))
        print("Berlaku hingga : ", (self.getActiveUntil()))
        print("Tipe kendaraan : ", (self.getVehicleType()))
     
        if self.getLicenseID() % 2 == 1:
            self.setPesawat(fly)
            self.showAirplane()
        else:
            self.setKapal(swim)
            self.showShip()


