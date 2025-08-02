/*
 * Saya Shafa Meira W. 2007723 mengerjakan tmd dalam mata kuliah
 * dpbo untuk keberkahan-Nya, maka saya tidak melakukan
 * kecurangan seperti yang telah dispesifikasikan. Aamiin
 */
package view;

//import java

import model.Koneksi;
import javax.swing.*;
import java.awt.*;

import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.ArrayList;
import java.util.Random;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.Timer;

/**
 *
 * @author shafa meira w.
 */
public class View implements ActionListener, MouseListener, KeyListener{

    /**
     * @param args the command line arguments
     */
    
    public static View tmd;
    
    public final int width = 800, height = 600;
    public final int lebar = -800, tinggi = -600;
    
    public Renderer renderer;
    
    public Rectangle orang, dasar;
    
    public ArrayList<Rectangle> columns;
    
    public int ticks, xMotion, yMotion, score, totalscore=0, fall;
    public int kenaColumn = 0, kenaDasar = 0;

    public boolean gameOver, started;
    
    public Random rand;
    
    public View(){

        Form1 form = new Form1();//jframe tabel

        JFrame jframe = new JFrame(); //deklarasi jframe
        Timer timer = new Timer(20, this);//deklarasi timer
        
        renderer = new Renderer();//deklarasi class renderer
        rand = new Random();//deklarasi random
        
        //konfigurasi awal jframe        
        jframe.add(renderer);
        jframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jframe.setSize(width, 640);
        jframe.addMouseListener(this);
        jframe.addKeyListener(this);
        jframe.setResizable(false);
                
        //deklarasi komponen game
        orang = new Rectangle(width / 2 - 10, height / 2 - 10, 20, 20);
        dasar = new Rectangle(0, 601, width, 1);
        columns = new ArrayList<Rectangle>();
        
        //pemanggilan awal fungsi penambahan kolom
        addColumn(true);
        addColumn(true);
        addColumn(true);
        
        //waktu dimulai
        timer.start();
        jframe.setVisible(true);
    }
    
    public static void main(String[] args) {
        // TODO code application logic here
        
        //memulai class View
        tmd = new View();
    }
    
    //fungsi untuk menambah kolom
    //seperti koordinat & ukuran
    public void addColumn(boolean start){
        int space = 100;
        int WIDTH = 60;
        int HEIGHT = 50 + rand.nextInt(300);
        
        int LEBAR = -100;
        
        int angka, kelipatan = 60, terlewati = 0, before = 0;  
        
        //ketika masih loop pertama
        //dibedakan sgsr pada loop kedua dst, jarak antar balok bisa ttp normal
        if(start){      
            for (int i = 0; i < 5; i++) {


                if(rand.nextInt(10) % 2 != 0 || before == 1){
                
                    angka = 50 + rand.nextInt(100);
                    columns.add(new Rectangle(orang.x + columns.size() * kelipatan, height - angka, WIDTH, angka));     
                    
                    if(terlewati != 0){
                        kelipatan = 60;
                        terlewati = 0;
                        before = 0;
                    }
                }
                else{
                    kelipatan = kelipatan + 60;
                    terlewati = 1;
                    before++;
                }
            }
        }
        else{
            for (int i = 0; i < 5; i++) {

                if(rand.nextInt(10) % 2 != 0 || before == 1){
                    angka = 50 + rand.nextInt(100);
                    columns.add(new Rectangle(columns.get(columns.size() - 1).x + kelipatan, height - angka, WIDTH, angka));      

                     if(terlewati != 0){
                        kelipatan = 60;
                        terlewati = 0;
                        before = 0;
                    }
                }
                else{
                    kelipatan = kelipatan + 60;
                    terlewati = 1;
                    before++;
                }
            }
        }        
    }
    
    //memberikan warna pada balok
    public void paintColumn(Graphics g, Rectangle column){
        g.setColor(Color.green.darker());
        g.fillRect(column.x, column.y, column.width, column.height);
    }

    //memberikan warna pada semua komponen game
    void repaint(Graphics g) {

        //background jframe
        g.setColor(Color.white);
        g.fillRect(0, 0, width, height);

        //komponen manusia
        g.setColor(Color.yellow);
        g.fillRect(orang.x, orang.y, orang.width, orang.height);

        //komponen dasar
        g.setColor(Color.red);
        g.fillRect(dasar.x, dasar.y, dasar.width, dasar.height);

        //loop untuk mewarnai semua balok
        for(Rectangle column : columns){
            paintColumn(g, column);
        }
        
            g.setColor(Color.red);
            g.setFont(new Font("Arial", 1, 70));
            
        //deklarasi statement ketika game mulai/selesai
        if(!started){
            g.drawString("Tekan Arrow Atas", 65, height/2 - 70);
        }
        if(gameOver){
            g.drawString("Selesai :(", 100, height/2 - 50);
        }
       
        g.setColor(Color.black);
        g.setFont(new Font("Arial", 1, 20));

        //komponen score
        if(!gameOver && started){
            if(score % 3 == 0){
                totalscore = (score/3)-1;
            }
            g.drawString("adapt:" + String.valueOf(score), 4, 25);
            g.drawString("fall:" + String.valueOf(fall), 4, 53);
        }

    }

    //proses ketika lompat
    public void jump(){
        //ketika game selesai
        if(gameOver){

            columns.clear();
            xMotion = 0; 
            yMotion = 0;
            score = 0;
            fall = 0;

            //inisialisasi ulang
            gameOver = false;
        }
        
        if(!started){
            started = true;
        }
        else if(!gameOver){
            if(yMotion > 0){
                yMotion = 0;
            }
            
            yMotion -= 10;
        }
    }
    
    //keselurahan proses game saat dimulai
    @Override
    public void actionPerformed(ActionEvent e) {
        int speed = 3;
        ticks++;
        
        if(started){
           
            for(int i = 0; i < columns.size(); i++){
                Rectangle column = columns.get(i);
                column.x -= speed; //kecepatan kolom bergeser
            }

            //koordinat manusia seiring bergerak
            if(ticks % 2 == 0 && yMotion < 15){
                yMotion += 1;
                xMotion += 0.5;
            }

            //loop remove column
            for(int i = 0; i < columns.size(); i++){
                Rectangle column = columns.get(i);

                if(column.x + column.width < 0){
                    columns.remove(column);
                    addColumn(false);
                }
            }

            //pergerakan manusia
            orang.x += xMotion;
            orang.y += yMotion;

            //loop untuk score & fall
            for(Rectangle column : columns){

                //manusia melewati kolom
                if( orang.x + orang.width / 2 > column.x + column.width / 2 - 10 && orang.x + orang.width /2 < column.x + column.width / 2 + 10){
                    score++; 
                    kenaColumn = 1;
                }
                // manusia jatuh
                if(orang.y + (orang.height/2) >= 600 && kenaColumn == 1){
                    fall++;
                    kenaColumn = 0;
                }
                
                //ketika manusia mengenai kolom, maka akan diam di x kolom
                if(column.intersects(orang)){

                    if(orang.x <= column.x){
                        orang.x = column.x - orang.width;
                    }
                    else{
                        if(column.y != 0){
                            orang.y = column.y - orang.height;
                        }
                    }
                    
                }
                
            }

            //ketika manusia lompat terlalu tinggi
            if( orang.y < 0){
                gameOver = true;
            }

            //pergerakan saat manusia jatuh
            if(orang.y  + yMotion >= height){
                orang.y = height - orang.height;
            }
        }

        //cat ulang
        renderer.repaint();
    }

    @Override
    public void mouseClicked(MouseEvent e) {
    }

    @Override
    public void mousePressed(MouseEvent e) {
    }

    @Override
    public void mouseReleased(MouseEvent e) {
    }

    @Override
    public void mouseEntered(MouseEvent e) {
    }

    @Override
    public void mouseExited(MouseEvent e) {
    }

    @Override
    public void keyTyped(KeyEvent e) {
    }

    @Override
    public void keyPressed(KeyEvent e) {
    }

    @Override
    public void keyReleased(KeyEvent e) {
        //ketika arrow atas ditekan
        if(e.getKeyCode() == KeyEvent.VK_UP){
            jump();
        }
        //ketika space ditekan
        if(e.getKeyCode() == KeyEvent.VK_SPACE){
            gameOver = true;

            //maka akan memasukan nilai ke database
            Koneksi koneksi = new Koneksi(score, fall);
        }
    }
}