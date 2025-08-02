#include <string>
#include <iostream>
#include <bits/stdc++.h>
#include "product.cpp"
#include "hardware.cpp"
#include "memory.cpp"

using namespace std;

int main(){

    // semua instansiasi dilakukan dgn method setter

    product produk;

    // deklarasi variabel
    int harga, frekuensi, ukuran;
    string id, merk, bentuk, cuda;

    // input
    cin >> harga >> id;

    produk.setPrice(harga);
    produk.setIdProduct(id);

    // output dgn getter
    cout << "==============================================" << endl;
    cout << "Harga : Rp" << produk.getPrice() << endl; 
    cout << "ID Produk : " << produk.getIdProduct() << endl; 

    hardware keras;

    cin >> merk >> bentuk;

    // child mengakses method parent product
    keras.setPrice(harga);
    keras.setIdProduct(id);
    keras.setBrand(merk);
    keras.setModel(bentuk);

    cout << "==============================================" << endl;
    cout << "Merek : " << keras.getBrand() << endl; 
    cout << "Model : " << keras.getModel() << endl; 
    cout << "Harga : Rp" << keras.getPrice() << endl; 
    cout << "ID Produk : " << keras.getIdProduct() << endl; 

    memory memori;

    cin >> frekuensi >> ukuran >> cuda;

    // child mengakses method parent product dan hardware
    memori.setPrice(harga);
    memori.setIdProduct(id);
    memori.setBrand(merk);
    memori.setModel(bentuk);
    memori.setFrequency(frekuensi);
    memori.setMemorySize(ukuran);
    memori.setSupportCuda(cuda);

    cout << "==============================================" << endl;
    cout << "Merek : " << memori.getBrand() << endl; 
    cout << "Model : " << memori.getModel() << endl; 
    cout << "ID Produk : " << memori.getIdProduct() << endl; 
    cout << "Frekuensi : " << memori.getFrequency() << "MHz" << endl; 
    cout << "Ukuran Memory : " << memori.getMemorySize() << "GB" << endl; 
    cout << "Support Cuda :" << memori.getMemorySize() << endl; 
    cout << "Harga : Rp" << memori.getPrice() << endl; 

    return 0;
}