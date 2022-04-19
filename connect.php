<?php

    $dbhost = 'localhost';
    $dbuser = 'root';
    $dbpass = '';
    $conn = mysqli_connect($dbhost, $dbuser, $dbpass);

    if(! $conn ){
        die('Could not connect: ' . mysqli_error($conn));
    }
    else{
        echo "connect succesfully\n";
    }

    $db_selected = mysqli_select_db($conn, 'db_utskelasweb');


    if(! $db_selected ){
        die('Can\'t use latihan : ' . mysqli_error($db_selected));
    }

    
    if ( mysqli_query($conn, "DESCRIBE `t_praklat2`") ) {
        echo "tabel udah ada";
    }

    else{
        $sql = "CREATE TABLE t_praklat2(
            id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            nama VARCHAR(255),
            email VARCHAR(255),
            alamat VARCHAR(300),
            ukuran VARCHAR(2),
            warna VARCHAR(255),
            kode_pos VARCHAR(10))"; 
        // Buat query create table disini

        $create = mysqli_query($conn, $sql);
        
        if($create){
            echo "<p>Table has been created</p>";
        }else{
            die('invalid query : ' . mysqli_error($create));
        }
    }
    
    // mysqli_close($conn);
    // return $conn;

?>