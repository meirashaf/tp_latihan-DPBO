<?php 
include("DB.php");

class Task extends DB{
	
	// Mengambil data
	function getTask(){
		// Query mysql select data ke tb_to_do
		$query = "SELECT * FROM pengurus";

		// Mengeksekusi query
		return $this->execute($query);
	}
	
	// menambah tugas baru
	function addTask(){
		// mengambil value dari masing2 tag
		$nim = $_POST['tnim'];		
		$nama = $_POST['tnama'];		
		$semester = $_POST['tsemester'];		
		$bidang = $_POST['tbidang'];		
		$foto = $_POST['tfoto'];		
		
		// query untuk menambahkan tugas
		$query = "INSERT INTO `pengurus` (`id_pengurus`, `nim`, `nama`, `semester`, `id_bidang`, `foto`) VALUES (NULL, '$nim', '$nama', '$semester', '$bidang', '$foto')";
		
		return $this->execute($query);
	}
	
	// menghapus tugas
	function delTask(){
		// mengambil value id row
		$id = $_GET['id_hapus'];
		// query untuk menghapus row
		$query = "DELETE FROM tb_to_do WHERE id = '$id'";

		return $this->execute($query);
	}

	// menandai tugas sebagai selesai
	function finishTask(){
		// mengambil value id row
		$id = $_GET['id'];
		$nim = $_POST['tnim'];		
		$nama = $_POST['tnama'];		
		$semester = $_POST['tsemester'];		
		$bidang = $_POST['tbidang'];		
		$foto = $_POST['tfoto'];		

		// query untuk mengubah status menjadi Sudah
		$query = "UPDATE `pengurus` SET `nim` = '$nim', `nama` = '$nama', `semester` = '$semester', `id_bidang` = '$bidang', `foto` = '$foto' WHERE id = '$id'";

		return $this->execute($query);
	}

}

?>