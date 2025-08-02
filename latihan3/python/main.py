#import kelas
from processor import processor
from disk import disk
from ram import ram
from pc import pc

# instansiasi dengan method constructor
otak = processor("Intel", 1200000)
cakram = disk("SDD", 12, 120000)
memory = ram(12, 1200000)

komputer = pc()

# menampilkan output
print("Processor")
print("Nama: %s" % (otak.getName()))
print("Harga: Rp%d" % (otak.getPrice()))

print("\nDisk")
print("Type: %s" % (cakram.getType()))
print("Kapasitas: %d" % (cakram.getCapacity()))
print("Harga: Rp%d" % (cakram.getPrice()))

print("\nRAM")
print("Kapasitas: %d" % (memory.getCapacity()))
print("Harga: Rp%d" % (memory.getPrice()))

total = otak.getPrice() + cakram.getPrice() + memory.getPrice()

komputer.setTotalPrice(total)

print("\n>>> Total Harga: Rp%d" % (komputer.getTotalPrice()))