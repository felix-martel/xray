<?php

$ID_ADMIN = 1;

// connexion à la base de donnée x-ray

$sql['user'] = "xray";
$sql['pwd'] = "#radio1pl3t3l#";
$sql['server'] = "localhost";
$sql['bdd'] = "xray";

mysql_connect($sql['server'], $sql['user'], $sql['pwd']);
mysql_select_db($sql['bdd']);
mysql_query("SET NAMES 'utf8'");

?>