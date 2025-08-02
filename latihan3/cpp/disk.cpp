class disk{

    private:
        // atribut
        string type;
        int capacity;
        int price;

    public:
        // konstruktor
        disk(){}

        disk(string type, int capacity, int price){
            this->type = type;
            this->capacity = capacity;
            this->price = price;
        }

        // setter dan getter
        void setTypeD(string type){ this->type = type; }
        string getTypeD(){ return this->type; }

        void setCapacityD(int capacity){ this->capacity = capacity; }
        int getCapacityD(){ return this->capacity; }

        void setPriceD(int price){ this->price = price; }
        int getPriceD(){ return this->price; }

        // destructor
        ~disk(){}
};