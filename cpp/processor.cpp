class processor{
    private:
        // atribut
        string name;
        int price;

    public:
        // konstruktor
        processor(){}
        
        processor(string n, int p){
            this->name = n;
            this->price = p;
        }

        // setter dan getter
        void setNameP(string name){ this->name = name; }
        string getNameP(){ return this->name; }

        void setPriceP(int price){ this->price = price; }
        int getPriceP(){ return this->price; }

        // destructor
        ~processor(){}
};