/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package tp1;

/**
 *
 * @author erric isnaini
 */
public class Author {
    private String penulis;
    private int jumlah_buku;
    private String foto;
    
    Author(){}
    
    Author(String penulis, int jumlah_buku, String foto){
        this.penulis = penulis;
        this.jumlah_buku = jumlah_buku;
        this.foto = foto;
    }
    
    public String getPenulis() {
        return penulis;
    }

    public void setPenulis(String penulis) {
        this.penulis = penulis;
    }

    public int getJumlah_buku() {
        return jumlah_buku;
    }

    public void setJumlah_buku(int jumlah_buku) {
        this.jumlah_buku = jumlah_buku;
    }

    public String getFoto() {
        return foto;
    }

    public void setFoto(String foto) {
        this.foto = foto;
    }

}
