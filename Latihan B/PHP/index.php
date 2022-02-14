<?php
    include "bola.php";

    // instansiasi dengan method constructor
    $satu = new bola("Persib", "Indonesia", 1967, "Irfan Bachdim");

    // instansiasi dengan method setter
    $dua = new bola();
    $dua->setNama("qwerty");
    $dua->setNegara("far far away");
    $dua->setTahun(2022);
    $dua->setPemain("Shrek");

    // menampilkan output dengan memanggil fungsi print
    echo $satu->print();
    
    // menampilkan output dengan memanggil fungsi getter
    echo "==============================================<br>";
    echo "Nama Tim: ".$dua->getNama()."<br>";
    echo "Negara asal : ".$dua->getNegara()."<br>";
    echo "Tahun berdiri: ".$dua->getTahun()."<br>";
    echo "Pemain : ".$dua->getPemain()."<br>";
?>
