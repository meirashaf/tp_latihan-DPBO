<?php 
    // include("DB.php");
    include("conf.php");
    include("Task.php");

    $otask = new Task($db_host, $db_user, $db_password, $db_name);
    $otask->open();

    if( !isset($_GET['id']) ){
        header('Location: index.html');
    }

    $id = $_GET['id'];
    $sql = "SELECT * FROM pengurus WHERE id_pengurus=$id";
    $data = mysqli_fetch_assoc($otask->execute($sql));

    if(mysqli_num_rows($otask->execute($sql)) < 1){
        die("Data tidak ditemukan...");
    }
    
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Belajar PHP</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light navbar-default" id="kustom">
        <div class="container-fluid">
            <a class="navbar-brand" href="index.php">
                <img src="kemakom.png" width="40" height="40">
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="true" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <a class="nav-link" href="form.html">Tambah Data</a>
                    <a class="nav-link" href="divisi.php">Divisi</a>
                    <a class="nav-link" href="bidang.php">Bidang</a>
                </div>
            </div>
        </div>
    </nav>

<div class="container-fluid p-0">
    <div class="card p-5 border-0">

        <form action="index.php" method="POST">
            <!-- NIM -->
            <div class="mb-3">
                <label for="tnim" class="form-label">NIM</label>
                <input name="tnim" type="number" class="form-control" id="exampleInputNIM1" value="<?php echo $data['nim'] ?>">
            </div>

            <!-- Nama -->
            <div class="mb-3">
                <label for="tnama" class="form-label">Nama</label>
                <input name="tnama" type="text" class="form-control" id="exampleInputNama1" value="<?php echo $data['nama'] ?>">
            </div>

            <!-- Semester -->
            <div class="form-row">
                <div class="form-group col">
                    <label for="tsemester">Semester</label>
                    <select name="tsemester" class="custom-select form-control">
                        <option selected>Pilih semester</option>
                        <option <?php if($data['semester'] == '1') echo 'selected';?> value="1">1</option>
                        <option <?php if($data['semester'] == '2') echo 'selected';?> value="2">2</option>
                        <option <?php if($data['semester'] == '3') echo 'selected';?> value="3">3</option>
                        <option <?php if($data['semester'] == '4') echo 'selected';?> value="4">4</option>
                        <option <?php if($data['semester'] == '5') echo 'selected';?> value="5">5</option>
                        <option <?php if($data['semester'] == '6') echo 'selected';?> value="6">6</option>
                    </select>
                </div>
            </div>

            <br>
            <!-- Bidang -->
            <div class="form-row">
                <div class="form-group col">
                    <label for="tbidang">Bidang</label>
                    <select name="tbidang" class="custom-select form-control">
                        <option selected>Pilih bidang</option>
                        <option <?php if($data['id_bidang'] == '1') echo 'selected';?> value="1">Ketua</option>
                        <option <?php if($data['id_bidang'] == '2') echo 'selected';?> value="2">Sekretaris</option>
                        <option <?php if($data['id_bidang'] == '3') echo 'selected';?> value="3">Bendahara</option>
                        <option <?php if($data['id_bidang'] == '4') echo 'selected';?> value="4">Staff</option>
                    </select>
                </div>
            </div>
        <br>
        <!-- foto -->
            <div class="mb-3">
                <label for="tfoto">Upload foto</label>
                <input name="tfoto" type="file" class="form-control" id="tfoto" value="<?php echo $data['foto'] ?>">
            </div>

            <button type="submit" class="btn btn-primary"  name="update" >Update</button>
        </form>
    </div>
</div>


</body>
</html>