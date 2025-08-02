#include <string>
#include <iostream>

using namespace std;

class bola{
    private:
        // atribut
        std::string nama, negara, pemain;
        int tahun;

    public:
        // constructor
        bola(){
            this->tahun = 0;
            this->nama = this->negara = this->pemain = "blank";
        }

        // constructor + parameter
        bola(string nama, string negara, int tahun, string pemain){
            this->nama = nama;
            this->negara = negara;
            this->tahun = tahun;
            this->pemain = pemain;
        }

        /*
            Setter dan Getter
        */ 

        void setNama(string nama){ //ini fungsinya cmn 1 atribut
			this->nama = nama;
		}
        string getNama(){
            return this->nama;
        }

        void setNegara(string negara){ //ini fungsinya cmn 1 atribut
			this->negara = negara;
		}
        string getNegara(){
            return this->negara;
        }

        void setTahun(int tahun){ //ini fungsinya cmn 1 atribut
			this->tahun = tahun;
		}
        int getTahun(){
            return this->tahun;
        }

        void setPemain(string pemain){ //ini fungsinya cmn 1 atribut
			this->pemain = pemain;
		}
        string getPemain(){
            return this->pemain;
        }

        // method menampilkan output
        void keluaran(){
            cout << "==============================================" << endl;
            cout << "Nama tim : " << this->nama << endl;
            cout << "Negara asal : " << this->negara << endl;
            cout << "Tahun berdiri : " << this->tahun << endl;
            cout << "Pemain : " << this->pemain << endl;
        }

        ~bola(){}

};
