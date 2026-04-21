<?php
echo "<h1>Liste des étudiants</h1>";


foreach ($students as $student) {
       echo "{$student['name']} - {$student['age']} ans<br>";

    }



?>