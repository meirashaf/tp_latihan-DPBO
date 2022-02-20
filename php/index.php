<?php
    include "memory.php";

    // instansiasi dengan method constructor
    $produk = new product(1200000, "SHDAJASD7");
    
    // menampilkan output dengan memanggil fungsi getter
    echo "==============================================<br>";
    echo "Harga : Rp".$produk->getPrice()."<br>";
    echo "ID Produk : ".$produk->getIdProduct()."<br>";
    
    // instansiasi dengan method setter
    $keras = new hardware();
    $keras->setPrice(1200000);
    $keras->setIdProduct("SHDAJASD7");
    $keras->setBrand("Acer");
    $keras->setModel("Aspire");
    
    // menampilkan output dengan memanggil fungsi getter
    echo "==============================================<br>";
    echo "Harga : Rp".$keras->getPrice()."<br>";
    echo "ID Produk : ".$keras->getIdProduct()."<br>";
    echo "Merk : ".$keras->getBrand()."<br>";
    echo "Model : ".$keras->getModel()."<br>";

    $memori = new memory();
    $memori->setPrice(1200000);
    $memori->setIdProduct("SHDAJASD7");
    $memori->setBrand("Acer");
    $memori->setModel("Aspire");
    $memori->setFrequency(1500);
    $memori->setMemorySize(8);
    $memori->setSupportCuda("Yes");
    
    // menampilkan output dengan memanggil fungsi getter
    echo "==============================================<br>";
    echo "Harga : Rp".$memori->getPrice()."<br>";
    echo "ID Produk : ".$memori->getIdProduct()."<br>";
    echo "Merk : ".$memori->getBrand()."<br>";
    echo "Model : ".$memori->getModel()."<br>";
    echo "Frekuensi : ".$memori->getFrequency()."HMz<br>";
    echo "Memory Size : ".$memori->getMemorySize()." GB<br>";
    echo "Support Cuda : ".$memori->getSupportCuda()."<br>";
?>