/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package tp1;

/**
 *
 * @author erric isnaini
 */
public class Buku {
    private String penulis;
    private String penerbit;
    private String deskripsi;
    private String foto;
    
    Buku(){}
    
    Buku(String penulis, String penerbit, String deskripsi, String foto){
        this.penulis = penulis;
        this.penerbit = penerbit;
        this.deskripsi = deskripsi;
        this.foto = foto;
    }
    
public String getPenulis() {
    return penulis;
}

public void setPenulis(String penulis) {
    this.penulis = penulis;
}

public String getPenerbit() {
    return penerbit;
}

public void setPenerbit(String penerbit) {
    this.penerbit = penerbit;
}

public String getDeskripsi() {
    return deskripsi;
}

public void setDeskripsi(String deskripsi) {
    this.deskripsi = deskripsi;
}

public String getFoto() {
    return foto;
}

public void setFoto(String foto) {
    this.foto = foto;
}

    
}
