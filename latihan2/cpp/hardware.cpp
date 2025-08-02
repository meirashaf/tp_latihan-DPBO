#include <string>
#include <iostream>

using namespace std;

class hardware : public product{ //parent adalah product
    private://atribut
        std::string brand, model;

    public:
        // constructor
        hardware(){
            this->brand = this->model = "blank";
        }

        // Setter dan Getter

        void setBrand(string brand){ //ini fungsinya cmn 1 atribut
			this->brand = brand;
		}
        string getBrand(){
            return this->brand;
        }

        void setModel(string model){ //ini fungsinya cmn 1 atribut
			this->model = model;
		}
        string getModel(){
            return this->model;
        }

        // destructor
        ~hardware(){}
};