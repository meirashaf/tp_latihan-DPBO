<?php
    include('connect.php');

    $sql = "SELECT * FROM `t_praklat2`";

    $check = mysqli_query($conn, $sql);

    if(!$check){
        die('Couldn\'t get data: ' . mysqli_error($check));
    }

    echo "<h1>Data</h1>";
    echo "<a href='form.html'> Tambah data </a>";
    echo "<table border='1'>
        <tr>
            <td>No.</td>
            <td>nama</td>
            <td>email</td>
            <td>alamat</td>
            <td>ukuran</td>
            <td>Warna</td>
            <td>kode pos</td>
            <td>Aksi</td>
        </tr>";
    $i = 1;
    while($row = mysqli_fetch_array($check, MYSQLI_ASSOC)){
        echo "<tr>";
        echo "<td> $i </td>";
        echo "<td> {$row['nama']} </td>";
        echo "<td> {$row['email']} </td>";
        echo "<td> {$row['alamat']} </td>";
        echo "<td> {$row['ukuran']} </td>";
        echo "<td> {$row['warna']} </td>";
        echo "<td> {$row['kode_pos']} </td>";
        echo "<td><a href='update_data.php?id={$row['id']}'> Edit </a> / 
        <a href='delete_data.php?id={$row['id']}'> Delete </a></td>";
        $i++;
    }
    echo "</table>";
    mysqli_close($conn);

?>