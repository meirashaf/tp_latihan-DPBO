class pc{
    private:
        // atribut
        int totalPrice;
        processor pObj;
        disk dObj;
        ram rObj;

    public:
        // konstruktor
        pc(){}

        pc(processor p, disk d, ram r){
            this->pObj = p;
            this->dObj = d;
            this->rObj = r;
            this->totalPrice = this->pObj.getPriceP() + this->dObj.getPriceD() + this->rObj.getPriceR();
        }

        // setter dan getter
        void setTotalPrice(int totalPrice){ this->totalPrice = totalPrice; }
        int getTotalPrice(){ return this->totalPrice; }

        void setProcessor(processor p){ this->pObj = p; }
        processor getProcessor(){ return this->pObj; }

        void setDisk(disk d){ this->dObj = d; }
        disk getDisk(){ return this->dObj; }

        void setRam(ram r){ this->rObj = r; }
        ram getRam(){ return this->rObj; }

        // metode print
        void print(){
            cout << "===== Processor =====" << endl;
            cout << "Merk: " << this->pObj.getNameP() << endl;
            cout << "Harga: " << this->pObj.getPriceP() << endl;
            cout << endl;

            cout << "===== Disk =====" << endl;
            cout << "Type: " << this->dObj.getTypeD() << endl;
            cout << "Kapasitas: " << this->dObj.getCapacityD() << endl;
            cout << "Harga: " << this->dObj.getPriceD() << endl;
            cout << endl;

            cout << "===== RAM =====" << endl;
            cout << "Kapasitas: " << this->rObj.getCapacityR() << endl;
            cout << "Harga: " << this->rObj.getPriceR() << endl;
            cout << endl;
        }
        
        // destructor
        ~pc(){}
        
};