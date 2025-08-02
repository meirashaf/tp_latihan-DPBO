<?php
    class processor{
        // atribut
        private $price = 0;
        private $name = "blank";
     
        // constructor
        function __construct($price=0, $name="blank"){
            $this->price = $price;
            $this->name = $name;
        }

        // Setter dan Getter

        function setPrice($price){
            $this->price = $price;
        }
        function getPrice(){
            return $this->price;
        }

        function setName($name){
            $this->name = $name;
        }
        function getName(){
            return $this->name;
        }

        // destructor
        function __destruct(){}

    }
?>