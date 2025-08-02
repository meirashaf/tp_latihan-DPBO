<?php
    class ram{
        // atribut
        private $price = 0;
        private $capacity = 0;
     
        // constructor
        function __construct($price=0, $capacity=0){
            $this->price = $price;
            $this->capacity = $capacity;
        }

        // Setter dan Getter

        function setPrice($price){
            $this->price = $price;
        }
        function getPrice(){
            return $this->price;
        }

        function setCapacity($capacity){
            $this->capacity = $capacity;
        }
        function getCapacity(){
            return $this->capacity;
        }

        // destructor
        function __destruct(){}

    }
?>