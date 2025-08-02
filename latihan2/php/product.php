<?php
    class product{
        // atribut
        private $price = 0;
        private $idProduct = "blank";
     
        // constructor
        function __construct($price=0, $idProduct="blank"){
            $this->price = $price;
            $this->idProduct = $idProduct;
        }

        // Setter dan Getter

        function setPrice($price){
            $this->price = $price;
        }
        function getPrice(){
            return $this->price;
        }

        function setIdProduct($idProduct){
            $this->idProduct = $idProduct;
        }
        function getIdProduct(){
            return $this->idProduct;
        }

        // destructor
        function __destruct(){}

    }
?>