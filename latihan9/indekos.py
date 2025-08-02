from hunian import Hunian

class Indekos(Hunian):
    # constructor, hanya menggunakan 1 parameter
    def __init__(self, nama_pemilik, nama_penghuni, luas_tanah=1):
        super().__init__("Indekos", nama_pemilik)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.luas_tanah = luas_tanah

    # method dokumen
    def get_dokumen(self):
        return  "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."
 
    #  method nama_pemilik
    def get_nama_pemilik(self):
        return self.nama_pemilik

    #  method nama_penghuni
    def get_nama_penghuni(self):
        return self.nama_penghuni

    #  method luas_tanah
    def get_luas_tanah(self):
        return self.luas_tanah

    #  summary tidak menggunakan parent class karena tidak ada jumlah parameter yang sesuai di parent
    def get_summary(self):
        return "Hunian Indekos." "\nPemilik: " + self.nama_pemilik + "\nPenghuni: " + self.nama_penghuni + "\nLuas tanah: " + str(self.luas_tanah) + " m^2"
