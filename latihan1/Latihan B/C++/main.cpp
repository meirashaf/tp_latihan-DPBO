#include <bits/stdc++.h>
#include "bola.cpp"
using namespace std;

int main(){
    // instansiasi dengan setter
    bola player1;
    player1.setNama("Persib");
    player1.setNegara("Indonesia");
    player1.setTahun(1967);
    player1.setPemain("Irfan Bachdim");

    // instansiasi dengan constructor
    bola player2("BTS", "Hybe", 2013, "AgustD");

    // instansiasi dengan input array
    int n, year;
    string team, country, name;
    cin >> n; //jumlah input
    bola arrPlayer[n];

    for (int i = 0; i < n; i++){

        // memasukan parameter
        cin >> team >> country >> year >> name;

        arrPlayer[i].setNama(team);
        arrPlayer[i].setNegara(country);
        arrPlayer[i].setTahun(year);
        arrPlayer[i].setPemain(name);
    }

    // menampilkan output dengan getter
    cout << "==============================================" << endl;
    cout << "Nama tim : " << player1.getNama() << endl;
    cout << "Negara asal : " << player1.getNegara() << endl;
    cout << "Tahun berdiri : " << player1.getTahun() << endl;
    cout << "Pemain : " << player1.getPemain() << endl;

    // menampilkan output dengan method keluaran
    player2.keluaran();

    for (int i = 0; i < n; i++){
        arrPlayer[i].keluaran();
    }

return 0;
}