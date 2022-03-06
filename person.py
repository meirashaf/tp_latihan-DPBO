# NIK, Name, Gender, sleep()

class person():
    # atribut
    __nik = 0
    __name = ";"
    __gender = ";"
    
    # constructor
    def __init__(self):
        self.__nik = 0
        self.__name = ";"
        self.__gender = ";"
    
    # atribut biasa
    def setPerson(self, nik, name, gender):
        self.__nik = nik
        self.__name = name
        self.__gender = gender

    # atribut objek
    def setOrang(self, orang):
        self.__nik = orang.__nik
        self.__name = orang.__name
        self.__gender = orang.__gender
        
    # setter dan getter

    def setNik(self, nik):
        self.__nik = nik
        
    def getNik(self):
        return self.__nik 

    def setNama(self, nama):
        self.__name = nama
        
    def getNama(self):
        return self.__name 

    def setGender(self, gender):
        self.__gender = gender
        
    def getGender(self):
        return self.__gender 

    def sleep(self):
        if self.getNik() % 2 == 1:
            print("%s sedang tidur" % (self.getNama()))
        else:
            print("%s sedang bangun" % (self.getNama()))

    # output
    def showPerson(self):
         print("Nama : ", (self.getNama()))
         print("NIK : ", (self.getNik()))
         print("Gender : ", (self.getGender()))
         self.sleep()