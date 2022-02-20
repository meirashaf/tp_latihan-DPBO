<?php
    include "hardware.php";

    class memory extends hardware{
        // atribut
        private $frequency = 0;
        private $memorySize = 0;
        private $supportCuda = "blank";

        // constructor
        function __construct(){}

        // Setter dan Getter

        function setFrequency($frequency){
            $this->frequency = $frequency;
        }
        function getFrequency(){
            return $this->frequency;
        }

        function setMemorySize($memorySize){
            $this->memorySize = $memorySize;
        }
        function getMemorySize(){
            return $this->memorySize;
        }

        function setSupportCuda($supportCuda){
            $this->supportCuda = $supportCuda;
        }
        function getSupportCuda(){
            return $this->supportCuda;
        }

        // destructor
        function __destruct(){}

    }
?>