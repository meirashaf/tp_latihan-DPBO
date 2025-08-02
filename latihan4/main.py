from vehicle import vehicle
from ship import ship
from airplane import airplane
from driver import driver
from person import person
from job import job

print("====Data Kendaraan====")

kendaraan = [vehicle() for i in range(5)]

kendaraan[0].setVehicle("Premium", 12)
kendaraan[1].setVehicle("Petromax", 5)
kendaraan[2].setVehicle("Solar", 24)
kendaraan[3].setVehicle("Avtur", 100)
kendaraan[4].setVehicle("Pertalite", 4)

for i in range(5):
    print("================================", i+1)
    kendaraan[i].move() 

print("\n====Data Kapal====")

kapal = [ship() for i in range(5)]

kapal[0].setShip("Premium", 12, 20, "Indonesia")
kapal[1].setShip("Petromax", 6, 30, "Italia")
kapal[2].setShip("Solar", 3, 5, "Holyshu")
kapal[3].setShip("Pertalite", 30, 23, "States")
kapal[4].setShip("Pertamax", 7, 23, "China")

for i in range(5):
    print("================================", i+1)
    kapal[i].showShip()

print("\n====Data Pesawat====")

pesawat = [airplane() for i in range(5)]

pesawat[0].setAirplane("Premium", 12, 20, 40)
pesawat[1].setAirplane("Petromax", 6, 30, 50)
pesawat[2].setAirplane("Solar", 3, 5, 48)
pesawat[3].setAirplane("Pertalite", 30, 23, 42)
pesawat[4].setAirplane("Pertamax", 7, 23, 46)


for i in range(5):
    print("================================", i+1)
    pesawat[i].showAirplane()

print("\n====Data Pengemudi====")

supir = [driver() for i in range(5)]
supir[0].setDriver(923762238, "2 Mei 2022", "tidak ada")
supir[1].setDriver(246475131, "13 April 2039", "saget mabur")
supir[2].setDriver(353875453, "45 Desember 0822", "mapay")
supir[3].setDriver(289274729, "Suka-suka pemerintah", "sae ngojay")
supir[4].setDriver(876357388, "idk", "running type")

for i in range(5):
    print("================================", i+1)
    supir[i].showDriver(kapal[i], pesawat[i])

print("\n====Data Orang====")
orang = [person() for i in range(5)]

orang[0].setPerson(1231121, "Shafa", "cw")
orang[1].setPerson(3274309, "Oisu", "perempuan")
orang[2].setPerson(8789483, "Jules", "gender fluid")
orang[3].setPerson(7262453, "Maddy", "girl")
orang[4].setPerson(1219382, "Ichigo", "Boy")

for i in range(5):
    print("================================", i+1)
    orang[i].showPerson()

print("\n====Data Pekerjaan====")
kerja = [job() for i in range(5)]

kerja[0].setJob(1231121, "Garuda", "Pilot")
kerja[1].setJob(2137187, "Titanic", "Nahkoda")
kerja[2].setJob(2872626, "Pirate", "Jack Sparrow")
kerja[3].setJob(7782872, "Air Asia", "Ryo")
kerja[4].setJob(3729829, "Kwangya", "Winter")

for i in range(5):
    print("================================", i+1)
    kerja[i].showJob(orang[i], supir[i], kapal[i], pesawat[i])



