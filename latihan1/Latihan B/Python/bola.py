class bola():
    # atribut
    __nama = "blank"
    __negara = "blank"
    __tahun = 0
    __pemain = "blank"

    # constructor
    def __init__(self, nama="blank", negara="blank", tahun=0, pemain="blank"):
        self.__nama = nama
        self.__negara = negara
        self.__tahun = tahun
        self.__pemain = pemain

    # Setter dan Getter

    def setNama(self, nama):
        self.__nama = nama
        
    def getNama(self):
        return self.__nama 

    def setNegara(self, negara):
        self.__negara = negara
        
    def getNegara(self):
        return self.__negara 

    def setTahun(self, tahun):
        self.__tahun = tahun
        
    def getTahun(self):
        return self.__tahun 

    def setPemain(self, pemain):
        self.__pemain = pemain
        
    def getPemain(self):
        return self.__pemain 

    # untuk menampilkan keluaran
    def keluaran(self):
        print ("==============================================")
        print ("Nama tim : %s" % (self.__nama)) 
        print ("Negara asal : %s" % (self.__negara)) 
        print ("Tahun berdiri : %d" % (self.__tahun)) 
        print ("Pemain : %s" % (self.__pemain)) 