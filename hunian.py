class Hunian():
    # constructor
    def __init__(self, jenis, nama_pemilik, jml_penghuni = 1, jml_kamar = 1, luas_tanah = 1):
        self.jenis = jenis
        self.nama_pemilik = nama_pemilik
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.luas_tanah = luas_tanah

    # method getter 

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_luas_tanah(self):
        return self.luas_tanah

    # method getter menggunakan pass karena sudah dibuat di child class

    def get_nama_pemilik(self):
        pass

    def get_dokumen(self):
        pass

    # summary untuk rumah + apartemen
    def get_summary(self):
        return "Hunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang." + "\nPemilik: " + self.nama_pemilik + "\nJumlah kamar: " + str(self.jml_kamar) + "\nLuas tanah: " + str(self.luas_tanah) + " m^2"