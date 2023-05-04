<?php
require __DIR__.'/vendor/autoload.php';
use Kreait\Firebase\Factory;
$factory = (new Factory)
    ->withServiceAccount('credentials.json')
    ->withDatabaseUri('https://katakata-cb1db-default-rtdb.firebaseio.com/');

    $database = $factory->createDatabase();
#https://www.youtube.com/watch?v=3aMqhRASh1c
?>