/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package view;

import model.Koneksi;
import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTable;



/**
 *
 * @author erric isnaini
 */
public class Form1 extends JFrame{
    
    JTable j;
    JFrame f;
    public Form1(){
        initialize();
    }

    //untuk kontainer table data score & username
    private void initialize() {
// Frame initialization
        f = new JFrame();
 
        // Frame Title
        f.setTitle("The Survive Hop");
 
        // Data to be displayed in the JTable
        String[][] data = {
            { "Shafa", "200", "1" },
            { "Meira", "100", "2" }
        };
 
        // Column Names
        String[] columnNames = { "Username", "Adapt", "Fall" };
 
        // Initializing the JTable
        j = new JTable(data, columnNames);
        j.setBounds(30, 40, 200, 300);
 
        // adding it to JScrollPane
        JScrollPane sp = new JScrollPane(j);
        f.add(sp);
        // Frame Size
        f.setSize(500, 200);
        // Frame Visible = true
        f.setVisible(true);
    }
    
    
}