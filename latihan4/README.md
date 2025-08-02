# LATIHAN4DPBO2022

Saya Shafa Meira W. 2007723 mengerjakan latihan 4 dalam mata kuliah DPBO untuk keberkahan-Nya, maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin


## Desain
Dibuat 6 kelas dengan atribut-atribut sebagai berikut:
1. Vehicle : fuelType, maxPassengers, Move()
2. Ship : age, type, countryOfManufacture
3. Airplane : type, age, wingsLength
4. Person : NIK, Name, Gender, sleep()
5. Job : NIP, companyName, position
6. Driver : lisenceID, activeUntil, vehicleType
<br>Pada setiap kelas dibuat deklarasi atribut, constructor, setter dan getter, serta untuk menampilkan output.

Program ini menggunakan prosedur **hybrid inheritance** yang merupakan gabungan dari hierarchical inheritance dan multiple inheritance, dengan rincian sebagai berikut:
- `vehicle` sebagai parent dari `ship` dan `airplane` karena ship dan airplane merupakan tipe kendaraan
- `ship` dan `airplane` sebagai parent dari `driver` karena driver adalah sebuah pekerjaan yang mengemudi sebuah kendaraan seperti ship atau airplane
- `driver` dan `person` sebagai parent dari `job` karena job terdiri dari identitas seorang person serta tipe pekerjaan yaitu driver/pengemudi

Program ini juga dibuat agar data dapat diturunkan melalui objek parameter, agar tidak perlu menulis data berulang kali. Desain dari program ini adalah seperti berikut, dengan ketentuan: kotak **merah** merupakan hierarchical inheritance dan kotak **biru** merupakan multiple inheritance. <br>
![image](https://user-images.githubusercontent.com/71260611/156938412-89bb13f2-1152-44d0-945b-975d668a5415.png)

### Data Vehicle
![image](https://user-images.githubusercontent.com/71260611/156936827-d560f2fc-e953-4c89-a717-433afc9fec28.png)

### Data Kapal
![image](https://user-images.githubusercontent.com/71260611/156936836-63040184-2ff0-4af1-b353-ee26b7061407.png)

### Data Pesawat
![image](https://user-images.githubusercontent.com/71260611/156936905-e20b9144-286e-4fb2-a522-aafd9da95833.png)

### Data Pengemudi
![image](https://user-images.githubusercontent.com/71260611/156937017-d234a9d2-28b1-4ad2-927f-34c0994edc53.png)
![image](https://user-images.githubusercontent.com/71260611/156937030-9683233f-8383-46ab-9bc7-ef5ea5ec82b2.png)

### Data Person
![image](https://user-images.githubusercontent.com/71260611/156936525-d1748a8f-0341-4f83-81fa-a436055951a7.png)

### Data Job
![image](https://user-images.githubusercontent.com/71260611/156936930-ff7a007a-5a00-4874-8700-ac3ea6949bdc.png)
![image](https://user-images.githubusercontent.com/71260611/156936946-982bffc7-bc38-458c-b843-3876f057500d.png)
![image](https://user-images.githubusercontent.com/71260611/156936960-ddddf6f3-0ee8-45c2-a6c9-130be2a04f6a.png)
