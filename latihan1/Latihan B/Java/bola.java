public class bola {
    // deklarasi variabel
    private int tahun;
    private String nama;
    private String negara;
    private String pemain;

    public bola(String nama, String negara, int tahun, String pemain){
        this.nama = nama;
        this.negara = negara;
        this.tahun = tahun;
        this.pemain = pemain;
    }

    public bola(){
    }

    /*
        Setter dan Getter
    */ 

    public int getTahun() {
        return tahun;
    }
    public void setTahun(int tahun) {
        this.tahun = tahun;
    }

    public String getNama() {
        return nama;
    }
    public void setNama(String nama) {
        this.nama = nama;
    }

    public String getNegara() {
        return negara;
    }
    public void setNegara(String negara) {
        this.negara = negara;
    }

    public String getPemain() {
        return pemain;
    }
    public void setPemain(String pemain) {
        this.pemain = pemain;
    } 

    // method untuk menampilkan output
    public void keluaran(){
        System.out.println("==============================================");
        System.out.println("Nama tim : " + this.nama);
        System.out.println("Negara asal : " + this.negara);
        System.out.println("Tahun berdiri : " + this.tahun);
        System.out.println("Pemain : " + this.pemain);
    }
}
