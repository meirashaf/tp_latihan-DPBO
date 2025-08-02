# LATIHAN2DPBO2022
Latihan ke-2 dari mata kuliah DPBO 2022

*Saya Shafa Meira W. 2007723 mengerjakan Latihan 2 dalam mata kuliah DPBO untuk keberkahan-Nya, maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin*

Disebabkan pada semua bahasa yang digunakan memiliki desain yang hampir sama, diputuskan untuk hanya membuat 1 file `README.md` yang sudah mencakup semua desain serta hasil program.

## Desain 
Dibuat class:
1. `product`, dengan atribut, yaitu price dan ID produk
2. `hardware`, dengan atribut, yaitu brand dan model
3. `memory`, dengan atribut, yaitu frekuensi, ukuran memory, serta support cuda

Program dirancang dengan `product` sebagai parent paling utama, lalu diikuti `hardware` sebagai child, dan terakhir yaitu `memory` sebagai child paling akhir. Dibuat fungsi constructor, setter dan getter, serta destructor untuk semua atribut yang ada. 

Selanjutnya pada file `index/main` diinstansiasi 3 objek sesuai dengan seluruh class yang ada. Semua instansiasi dilakukan menggunakan method setter. Pertama, parent mengakses method yang dimiliki sendiri, hingga seterusnya child mengakses method miliknya sendiri serta semua method yang dimiliki oleh parent-parentnya. Terakhir, dipanggil fungsi print dan getter untuk menampilkan output.

Rancangan inheritance class:<br>
<img width="170" alt="image" src="https://user-images.githubusercontent.com/71260611/154809858-43092903-f750-484f-b5ff-0832a39ff9a9.png">

## Java<br>
<img width="244" alt="image" src="https://user-images.githubusercontent.com/71260611/154812241-101a0df8-d58b-47ae-bf58-7d387253bc17.png">

## C++<br>
<img width="188" alt="image" src="https://user-images.githubusercontent.com/71260611/154815810-dbdd184b-78b7-4d5a-8614-960690b2fd19.png">

## Python<br>
<img width="200" alt="image" src="https://user-images.githubusercontent.com/71260611/154841604-76d2963a-f3ba-4e32-8b68-c9429e66cbaa.png">

## PHP<br>
<img width="182" alt="image" src="https://user-images.githubusercontent.com/71260611/154847231-05a95328-d1d0-4dd0-b987-382a6c126913.png">
