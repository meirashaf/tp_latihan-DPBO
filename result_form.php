<?php 
    include('connect.php');
    if(isset($_POST['add'])){
        $nama = $_POST['nama'];
        $email = $_POST['email'];
        $alamat = $_POST['alamat'];
        $size = $_POST['size'];
        $warna = $_POST['color'];
        $kode_pos = $_POST['zip'];

        $sql = "INSERT INTO `t_praklat2` (`id`, `nama`, `email`, `alamat`, `ukuran`, `warna`, `kode_pos`) VALUES (NULL, '$nama', '$email', '$alamat', '$size', '$warna', '$kode_pos')"; // buat query insert data disini

        $result = mysqli_query($conn, $sql);
        if($result){
            echo "<p>Input Succesfully</p>";
            echo "<p><a href='home.php'>Kembali ke daftar</a></p>";
        }else{
            die('invalid query : ' . mysqli_error($result));
        }

        mysqli_close($conn);
    }
?>