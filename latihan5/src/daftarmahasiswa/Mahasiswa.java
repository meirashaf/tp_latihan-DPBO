/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package daftarmahasiswa;

/**
 *
 * @author LENOVO
 */
public class Mahasiswa {
    private String txtNIM;
    private String txtNama;
    private String txtNilai;
    
    public Mahasiswa(String n1, String n2, String n3){
        txtNIM = n1;
        txtNama = n2;
        txtNilai = n3;
    }
    
    public void setNim(String n) {
        txtNIM = n;
    }
    
    public void setNama(String n) {
        txtNama = n;
    }
    
    public void setNilai(String n) {
        txtNilai = n;
    }
    
    public String getNim() {
        return txtNIM;
    }
    
    public String getNama() {
        return txtNama;
    }
    
    public String getNilai() {
        return txtNilai;
    }
}