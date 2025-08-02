#include <string>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

#include "processor.cpp"
#include "disk.cpp"
#include "ram.cpp"
#include "pc.cpp"

int main(){
		
	processor otak("Intel", 120000); //buat objek processor
	disk cakram("SDD", 12, 9000); //buat objek disk
	ram memory(12, 2000000); //buat objek ram

	// buat objek pc lalu objek processor, disk, dan ram dimasukkan
	pc komputer(otak, cakram, memory);

	// menampilkan seluruh atribut pada semua objek yang ada
	komputer.print();

	cout << ">>> Total harga: Rp" << komputer.getTotalPrice() << endl;

	return 0;
}