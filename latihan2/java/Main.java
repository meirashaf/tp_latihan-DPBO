import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // Semua instansiasi menggunakan metode setter

        product produk = new product();

        // deklarasi variabel
        int harga, frekuensi, ukuran;
        String id, merek, bentuk, cuda;

        // instansiai objek Scanner untuk input
        Scanner sc = new Scanner(System.in);
        
        // input untuk class product (orang tua)
        harga = sc.nextInt();
        id = sc.next();
        
        // memasukkan input melalui setter
        produk.setPrice(harga);
        produk.setIdProduct(id);
        
        // menampilkan output dgn metode getter untuk class parent
        System.out.println("==============================================");
        System.out.println("Harga : Rp" + produk.getPrice());        
        System.out.println("ID Produk : " + produk.getIdProduct());        
        
        hardware keras = new hardware();
        
        // memasukkan input melalui setter
        merek = sc.next();
        bentuk = sc.next();
        
        keras.setBrand(merek);
        keras.setModel(bentuk);
        keras.setPrice(harga);
        keras.setIdProduct(id);
        
        // menampilkan output dgn metode getter untuk class child
        System.out.println("==============================================");
        System.out.println("Merek : " + keras.getBrand());        
        System.out.println("Model : " + keras.getModel());        
        System.out.println("Harga : Rp" + keras.getPrice());        
        System.out.println("ID Produk : " + keras.getIdProduct());  
        
        memory chip = new memory();
        
        // memasukkan input melalui setter
        frekuensi = sc.nextInt();
        ukuran = sc.nextInt();
        cuda = sc.next();
        
        chip.setFrequency(frekuensi);
        chip.setMemorySize(ukuran);
        chip.setSupportsCuda(cuda);
        chip.setBrand(merek);
        chip.setModel(bentuk);
        chip.setPrice(harga);
        chip.setIdProduct(id);
        
        // menampilkan output dgn metode getter untuk class child
        System.out.println("==============================================");
        System.out.println("Merek : " + chip.getBrand());        
        System.out.println("Model : " + chip.getModel());        
        System.out.println("ID Produk : " + chip.getIdProduct());  
        System.out.println("Frekuensi : " + chip.getFrequency() + "MHz");        
        System.out.println("Ukuran Memory : " + chip.getMemorySize() + "GB");        
        System.out.println("Support Cuda : " + chip.getSupportsCuda());        
        System.out.println("Harga : Rp" + chip.getPrice());        

    }
}
// bola player1 = new bola();
// player1.setNama("Aespa");
// player1.setNegara("Kroya");
// player1.setTahun(2013);
// player1.setPemain("Karina");