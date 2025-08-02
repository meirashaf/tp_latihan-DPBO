import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // instansiasi objek sesuai dengan menggunakan method constructor
        processor otak = new processor(120000, "Intel");
        disk cakram = new disk("SDD", 12, 120000);
        ram memory = new ram(23, 230000);

        pc komputer = new pc(otak, cakram, memory);

        // menampilkan output
        komputer.print();

        // menggunakan method untuk menguji konsep composition
        System.out.println("\n>>> Total harga: " + komputer.getTotalPrice());
    }
}