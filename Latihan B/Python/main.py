from bola import bola

# menggunakan setter
player1 = bola()
player1.setNama("Persib")
player1.setNegara("Indonesia")
player1.setTahun(1967)
player1.setPemain("Irfan Bachdim")

# menggunakan constructor
player2 = bola("BTS", "Korea Selatan", 2013, "Kim Namjoon")

n = int(input()) #menerima jumlah input

# alokasi & instansiasi objek array
arrPlayer = [bola() for i in range(n)]

# menerima input parameter dan instansiasi dengan setter
for i in range(n):
    name = input()
    country = input()
    year = int(input())
    person = input()

    arrPlayer[i].setNama(name)
    arrPlayer[i].setNegara(country)
    arrPlayer[i].setTahun(year)
    arrPlayer[i].setPemain(person)

# menampilkan output 
player1.keluaran() 

# dengan method getter
print ("==============================================")
print ("Nama tim : %s" % (player2.getNama())) 
print ("Negara asal : %s" % (player2.getNegara())) 
print ("Tahun berdiri : %d" % (player2.getTahun())) 
print ("Pemain : %s" % (player2.getPemain())) 

# menampilkan output array objek
for i in range(n):
    arrPlayer[i].keluaran()