<?php
    class mahasiswa{
        // atribut
        private $Nama = "Nama";
        private $NIM = 0;
        private $jenisKelamin = "jenisKelamin";
        private $prodi = "prodi";
        private $Semester = 0;    

        // constructor
        public function __construct($Nama="Nama", $NIM=0, $jenisKelamin="jenisKelamin", $prodi="prodi", $Semester=0){
            $this->Nama = $Nama;
            $this->NIM = $NIM;
            $this->jenisKelamin = $jenisKelamin;
            $this->prodi = $prodi;
            $this->Semester = $Semester;
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

        public function setNIM($NIM){
            $this->NIM = $NIM;
        }
        public function getNIM(){
            return $this->NIM;
        }

        public function setJenisKelamin($jenisKelamin){
            $this->jenisKelamin = $jenisKelamin;
        }
        public function getJenisKelamin(){
            return $this->jenisKelamin;
        }

        public function setProdi($prodi){
            $this->prodi = $prodi;
        }
        public function getProdi(){
            return $this->prodi;
        }

        public function setSemester($Semester){
            $this->Semester = $Semester;
        }
        public function getSemester(){
            return $this->Semester;
        }

        // untuk menampilkan semua atribut per objek
        public function print(){
            echo "==============================================<br>";
            echo "Nama : ".$this->Nama."<br>";
            echo "NIM : ".$this->NIM."<br>";
            echo "Jenis Kelamin : ".$this->jenisKelamin."<br>";
            echo "Program Studi : ".$this->prodi."<br>";
            echo "Semester : ".$this->Semester."<br>";
        }
    }
?>