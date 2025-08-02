from hardware import hardware

class memory(hardware):
    # atribut
    __frequency = 0
    __memorySize = 0
    __supportCuda = "blank"

    # constructor
    def __init__(self, supportCuda="blank", frequency=0, memorySize=0):
        self.__frequency = frequency
        self.__memorySize = memorySize
        self.__supportCuda = supportCuda
      
    # Setter dan Getter

    def setFrequency(self, frequency):
        self.__frequency = frequency
        
    def getFrequency(self):
        return self.__frequency 

    def setMemorySize(self, memorySize):
        self.__memorySize = memorySize
        
    def getMemorySize(self):
        return self.__memorySize 

    def setSupportCuda(self, supportCuda):
        self.__supportCuda = supportCuda
        
    def getSupportCuda(self):
        return self.__supportCuda 
