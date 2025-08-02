class ram{
    private:
        // atribut
        int price, capacity;

    public:
        // konstruktor
        ram(){}

        ram(int capacity, int price){
            this->capacity = capacity;
            this->price = price;
        }

        // setter dan getter
        void setCapacityR(int capacity){ this->capacity = capacity; }
        int getCapacityR(){ return this->capacity; }

        void setPriceR(int price){ this->price = price; }
        int getPriceR(){ return this->price; }

        // destructor
        ~ram(){}
};