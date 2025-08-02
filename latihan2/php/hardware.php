<?php
    include "product.php";

    class hardware extends product{
        // atribut
        private $brand = "blank";
        private $model = "blank";
    
        // constructor
        function __construct(){}

        // Setter dan Getter

        function setBrand($brand){
            $this->brand = $brand;
        }
        function getBrand(){
            return $this->brand;
        }

        function setModel($model){
            $this->model = $model;
        }
        function getModel(){
            return $this->model;
        }
        
        // destructor
        function __destruct(){}

    }
?>