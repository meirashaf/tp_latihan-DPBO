<?php
    include "mahasiswa.php";

    // menginstansiasi objek
    $satu = new mahasiswa("Shafa Meira W.", 2007723, "Perempuan", "Ilmu Komputer", 4);
    $dua = new mahasiswa("Alfi Amaliandini", 2005647, "Perempuan", "Matematika", 5);
    $tiga = new mahasiswa("M. Rayzahran", 2001219, "Laki-laki", "Hubungan Internasional", 2);
    $empat = new mahasiswa("Dhiandra Latifa", 2009892, "Perempuan", "Desain dan Komunikasi Visual", 3);

    // menampilkan output dengan memanggil fungsi print
    echo $satu->print();
    echo $dua->print();
    echo $tiga->print();
    echo $empat->print();
?>