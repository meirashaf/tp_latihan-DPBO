from hunian import Hunian

class Apartemen(Hunian):
    # constructor
    def __init__(self, jenis, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah):
        super().__init__(jenis, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah)
        self.jenis = jenis
        self.nama_pemilik = nama_pemilik

    # method declare dokumen
    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    # method nama_pemilik
    def get_nama_pemilik(self):
        return self.nama_pemilik

    # method jenis
    def get_jenis(self):
        return self.jenis