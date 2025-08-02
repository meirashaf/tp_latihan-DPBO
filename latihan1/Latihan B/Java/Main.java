import java.util.*;

public class Main {
    public static void main(String[] args) {
      
        // instansiasi menggunakan setter
        bola player1 = new bola();
        player1.setNama("Aespa");
        player1.setNegara("Kroya");
        player1.setTahun(2013);
        player1.setPemain("Karina");
        
        // instansiasi menggunakan constructor
        bola player2 = new bola("Iz*one", "Bandung", 2019, "Wonyoung");
        
        int n; //menerima jumlah inputan
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        bola[] arrPlayer = new bola[n];
        
        int i, year=0;
        String team="x", country="x", name="x";
        
        // input nama tim, negara asal, tahun, dan pemain
        for(i=0; i<n; i++){
            //digunakan untuk mengatasi error ketika nextLine ter-skip
            if (i == 0) { 
                sc.nextLine();
            } 
            
            try {
                team = sc.nextLine();
            }catch(Exception e){}
            try {
                country = sc.nextLine();
            }catch(Exception e){}
            try {
                year = sc.nextInt();
            }catch(Exception e){}
            
            //digunakan untuk mengatasi error ketika nextLine ter-skip
            sc.nextLine();
            
            try {
                name = sc.nextLine();
            }catch(Exception e){}
            
            // instansiasi array objek
            arrPlayer[i] = new bola(team, country, year, name);
        }

        // output dengan cara getter
        System.out.println("==============================================");
        System.out.println("Nama tim : " + player1.getNama());
        System.out.println("Negara asal : " + player1.getNegara());
        System.out.println("Tahun berdiri : " + player1.getTahun());
        System.out.println("Pemain : " + player1.getPemain());
       
        // output dengan method
        player2.keluaran();
        
        for(i=0; i<n; i++){
            arrPlayer[i].keluaran();
        }
    }
}