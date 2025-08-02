<!-- Saya Shafa Meira W. 2007723 mengerjakan Latihan 7 PHP GUI dalam mata kuliah
DPBO untuk keberkahan-Nya, maka saya tidak melakukan
kecurangan seperti yang telah dispesifikasikan. Aamiin -->

<?php

include("conf.php");
include("Task.php");
include("Template.php");
// include("update")

// Membuat objek dari kelas task
$otask = new Task($db_host, $db_user, $db_password, $db_name);
$otask->open();

// button menambahkan
if(isset($_POST['add'])){
	$otask->addTask();
}
else if(isset($_POST['update'])){
	$otask->finishTask();
}


// Memanggil method getTask di kelas Task
$otask->getTask();

// Proses mengisi tabel dengan data
$data = null;
$no = 1;
$keterangan = " ";

while (list($id, $tnim, $tnama, $tsemester, $tbidang, $tfoto) = $otask->getResult()) {
    if($tbidang == 1){
        $keterangan = "Ketua"; 
    }
    else if($tbidang == 2){
        $keterangan = "Sekretaris"; 
    }
    else if($tbidang == 3){
        $keterangan = "Bendahara"; 
    }
    else if($tbidang == 4){
        $keterangan = "Staff";
    }

    $data .= "
    <div class='card border-2 m-4' style='width: 14rem;'>
        <a href='update_form.php?id=" . $id . "'>
            <img class='card-img-top mt-3' src=" . $tfoto . ">
        </a>
        <div class='card-body'>
            <h5 class='card-title'>" . $tnama . "</h5>
            " . $tnim . " <br>
            " . $keterangan . "
        </div>
    </div>";
}

// Menutup koneksi database
$otask->close();

// Membaca template skin.html
$tpl = new Template("index.html");

// Mengganti kode Data_Tabel dengan data yang sudah diproses
$tpl->replace("DATA_PENGURUS", $data);

// // Menampilkan ke layar
$tpl->write();