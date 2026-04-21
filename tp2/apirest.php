<?php
require_once 'config/config.php';
require_once 'services/StudentService.php';
$url = API_BASE_URL."/students";

$response = file_get_contents($url);


// Décodage du JSON en tableau PHP
// $students = json_decode($response, true);


$students =StudentService::getAllStudents();
require_once 'views/students.php';

?>
