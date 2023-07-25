/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import javax.swing.table.DefaultTableModel;

/**
 *ResultSet;
//import java.sql.Statement
 * @author erric isnaini
 */
public class Koneksi {
    public static Connection con;
    public static Statement stm;
        
    //konstruktor
    public Koneksi(int score, int fall){//untuk membuka koneksi ke database
        try {
            
            //koneksi ke db
            String url ="jdbc:mysql://localhost:3306/db_latihan_dpo";
            String user="root";
            String pass="";
            Class.forName("com.mysql.jdbc.Driver");
            con = DriverManager.getConnection(url,user,pass);
            stm = con.createStatement();
            
            //query insert
            String sql = "INSERT INTO texperiences VALUES(null, "+score+", "+fall+")";
            
            stm.executeUpdate(sql);
            
            System.out.println("koneksi berhasil;");
            con.close();
        } catch (Exception e) {
            System.err.println("koneksi gagal " +e.getMessage());
        }
    }
 
}
