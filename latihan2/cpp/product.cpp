#include <string>
#include <iostream>

using namespace std;

class product{
    private: //atribut
        std::string idProduct;
        int price;


    public:
        // constructor
        product(){
            this->price =0;
            this->idProduct ="blank";
        }

        // Setter dan Getter

        string getIdProduct() {
            return this->idProduct;
        }

        void setIdProduct(string idProduct) {
            this->idProduct = idProduct;
        }

        int getPrice() {
            return this->price;
        }

        void setPrice(int price) {
            this->price = price;
        }

        // destructor
        ~product(){}
};