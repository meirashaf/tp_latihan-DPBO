# Job : NIP, companyName, position
from driver import driver
from person import person

class job(driver, person):
    # atribut
    __nip = 0
    __companyName = ";"
    __position = ";"

    # constructor
    def __init__(self):
        self.__nip = 0
        self.__companyName = "."
        self.__position = ";"

    # atribut biasa
    def setJob(self, nip, companyName, position):
        self.__nip = nip
        self.__companyName = companyName
        self.__position = position

    # setter dan getter

    def setNip(self, nip):
        self.__nip = nip
        
    def getNip(self):
        return self.__nip 

    def setCompanyName(self, companyName):
        self.__companyName = companyName
        
    def getCompanyName(self):
        return self.__companyName 
    
    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position 

    # output
    def showJob(self, orang, supir, swim, fly):
        self.setOrang(orang)
        self.showPerson()

        print("NIP : %d" % (self.getNip()))
        print("Perusahaan : %s" % (self.getCompanyName()))
        print("Posisi : %s" % (self.getPosition()))

        self.setSupir(supir)
        self.showDriver(swim, fly)
        
