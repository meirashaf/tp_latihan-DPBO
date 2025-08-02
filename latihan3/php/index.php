<?php

    include "processor.php";
    include "disk.php";
    include "ram.php";
    include "pc.php";

    // instansiasi dgn method constructor
    $otak = new processor(120000, "Intel");
    $cakram = new disk("SDD", 12, 120000);
    $memory = new ram(12, 1200000);

    $komputer = new pc($otak, $cakram, $memory);

    // menampilkan output
    echo "Processor<br>";
    echo "Nama : ".$otak->getName()."<br>";
    echo "Harga : Rp".$otak->getPrice()."<br>";

    echo "<br>Disk<br>";
    echo "Type : ".$cakram->getType()."<br>";
    echo "Kapasitas : ".$cakram->getCapacity()."<br>";
    echo "Harga : Rp".$cakram->getPrice()."<br>";

    echo "<br>RAM<br>";
    echo "Kapasitas : ".$memory->getCapacity()."<br>";
    echo "Harga : Rp".$memory->getPrice()."<br>";
    
    $komputer->setTotalPrice($otak->getPrice() + $cakram->getPrice() + $memory->getPrice());    
    
    echo "<br> >>>> Total harga : Rp".$komputer->getTotalPrice()."<br>";
?>