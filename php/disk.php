<?php
    class disk{
        // atribut
        private $type = "blank";
        private $capacity = 0;
        private $price = 0;
     
        // constructor
        function __construct($type="blank", $capacity=0, $price=0){
            $this->type = $type;
            $this->capacity = $capacity;
            $this->price = $price;
        }

        // Setter dan Getter

        function setType($type){
            $this->type = $type;
        }
        function getType(){
            return $this->type;
        }

        function setCapacity($capacity){
            $this->capacity = $capacity;
        }
        function getCapacity(){
            return $this->capacity;
        }

        function setPrice($price){
            $this->price = $price;
        }
        function getPrice(){
            return $this->price;
        }

        // destructor
        function __destruct(){}

    }
?>