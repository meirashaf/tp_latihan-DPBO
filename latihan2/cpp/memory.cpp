#include <string>
#include <iostream>

using namespace std;

class memory : public hardware{//parent adalah hardware
    private://atribut
        int frequency, memorySize;
        std::string supportCuda;
    
    public:
        // constructor
        memory(){
            this->frequency = this->memorySize = 0;
            this->supportCuda = "blank";
        }
        
        // Setter dan Getter

        void setSupportCuda(string supportCuda){ //ini fungsinya cmn 1 atribut
			this->supportCuda = supportCuda;
		}
        string getSupportCuda(){
            return this->supportCuda;
        }

        void setFrequency(int frequency){ //ini fungsinya cmn 1 atribut
			this->frequency = frequency;
		}
        int getFrequency(){
            return this->frequency;
        }

        void setMemorySize(int memorySize){ //ini fungsinya cmn 1 atribut
			this->memorySize = memorySize;
		}
        int getMemorySize(){
            return this->memorySize;
        }

        // destructor
        ~memory(){}
};