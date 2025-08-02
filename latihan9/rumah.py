from hunian import Hunian

class Rumah(Hunian):
    # constructor
    def __init__(self, jenis, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah):
        super().__init__(jenis, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah)
        self.jenis = jenis
        self.nama_pemilik = nama_pemilik

    # dokumen method
    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    # nama_pemilik method
    def get_nama_pemilik(self):
        return self.nama_pemilik