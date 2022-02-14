<?php
    class bola{
        // atribut
        private $Nama = "Nama";
        private $Negara = "Negara";
        private $Tahun = 0;
        private $Pemain = "Pemain";

        // constructor
        public function __construct($Nama="Nama", $Negara="Negara", $Tahun=0, $Pemain="Pemain"){
            $this->Nama = $Nama;
            $this->Negara = $Negara;
            $this->Tahun = $Tahun;
            $this->Pemain = $Pemain;
        }

        /*
            Setter dan Getter
        */ 

        public function setNama($Nama){
            $this->Nama = $Nama;
        }
        public function getNama(){
            return $this->Nama;
        }
        
        public function setNegara($Negara){
            $this->Negara = $Negara;
        }
        public function getNegara(){
            return $this->Negara;
        }

        public function setTahun($Tahun){
            $this->Tahun = $Tahun;
        }
        public function getTahun(){
            return $this->Tahun;
        }

        public function setPemain($Pemain){
            $this->Pemain = $Pemain;
        }
        public function getPemain(){
            return $this->Pemain;
        }

        // untuk menampilkan keluaran
        public function print(){
            echo "==============================================<br>";
            echo "Nama Tim: ".$this->Nama."<br>";
            echo "Negara asal : ".$this->Negara."<br>";
            echo "Tahun berdiri: ".$this->Tahun."<br>";
            echo "Pemain : ".$this->Pemain."<br>";
        }          

        // destructor
        public function __destruct(){
        }
    }
?>