<?php 
    include('connect.php');
    $id = $_GET['id'];

    $sql = "DELETE FROM `t_praklat2` WHERE id = $id"; // buat query update data disini

    $query_user = mysqli_query($conn,$sql);

    if (mysqli_affected_rows($conn)>0) {
        //alihkan ke halaman home.php
        header('Location: home.php');
    }else{
        //tampilkan pesan gagal
        // die("Gagal menyimpanan perubahan...");
        die('invalid query: ' . mysqli_error($query_user));
    }
?>