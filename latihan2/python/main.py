from product import product
from hardware import hardware
from memory import memory

# menerima input
harga = int(input())
id = input()

# instansiasi dgn method setter
produk = product()
produk.setPrice(harga)
produk.setIdProduct(id)

# output dgn method getter
print ("==============================================")
print ("Harga : Rp%d" % (produk.getPrice())) 
print ("ID Produk : %s" % (produk.getIdProduct())) 

merk = input()
bentuk = input()

keras = hardware()
keras.setPrice(harga)
keras.setIdProduct(id)
keras.setBrand(merk)
keras.setModel(bentuk)

# output dgn method getter
print ("==============================================")
print ("Harga : Rp%d" % (keras.getPrice())) 
print ("ID Produk : %s" % (keras.getIdProduct())) 
print ("Merk : %s" % (keras.getBrand())) 
print ("Model : %s" % (keras.getModel())) 

frekuensi = int(input())
ukuran = int(input())
cuda = input()

memori = memory()
memori.setPrice(harga)
memori.setIdProduct(id)
memori.setBrand(merk)
memori.setModel(bentuk)
memori.setFrequency(frekuensi)
memori.setMemorySize(ukuran)
memori.setSupportCuda(cuda)

# output dgn method getter
print ("==============================================")
print ("Harga : Rp%d" % (memori.getPrice())) 
print ("ID Produk : %s" % (memori.getIdProduct())) 
print ("Merk : %s" % (memori.getBrand())) 
print ("Model : %s" % (memori.getModel())) 
print ("Frekuensi : %d MHz" % (memori.getFrequency())) 
print ("Ukuran Memory : %d GB" % (memori.getMemorySize())) 
print ("Support Cuda : %s" % (memori.getSupportCuda())) 