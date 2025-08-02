<?php
    class pc{
        // atribut
        private processor $pObj;
        private disk $dObj;
        private ram $rObj;
        private $totalPrice = 0;
     
        // constructor
        function __construct($pObj = processor, $dObj = disk, $rObj = ram){
            $this->pObj = $pObj;
            $this->dObj = $dObj;
            $this->rObj = $rObj;
            $this->totalPrice = 0;
        }

        // Setter dan Getter

        function setpObj($pObj){
            $this->pObj = $pObj;
        }
        function getpObj(){
            return $this->pObj;
        }

        function setdObj($dObj){
            $this->dObj = $dObj;
        }
        function getdObj(){
            return $this->dObj;
        }

        function setrObj($rObj){
            $this->rObj = $rObj;
        }
        function getrObj(){
            return $this->rObj;
        }

        function setTotalPrice($totalPrice){
            $this->totalPrice = $totalPrice;
        }
        function getTotalPrice(){
            return $this->totalPrice;
        }

        // destructor
        function __destruct(){}

    }
?>