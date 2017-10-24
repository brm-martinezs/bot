<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);
require('class/classMongo.php');

$alertMongo= new AlertMongo();

$mongo = new MongoDB\Driver\Manager('mongodb://brm2_us3r4pp:JLGhYDdMXIrI8y3n@127.0.0.1/callaut');

/* Crear colecciones
$cmd = new \MongoDB\Driver\Command([
    'aggregate' => 'tweetsend'
]);

$rows = $mongo->executeCommand('callaut',  $cmd);
foreach($rows as $r){
    print_r($r);
}*/

/*Listar Colecciones*/
$cmd = new \MongoDB\Driver\Command(['listCollections' => 1]);
$res = $mongo->executeCommand('callaut', $cmd);

$posts = [];
foreach ($res as $document) {
$alertMongo->printVar($document);
//die();
    array_push($posts, json_decode(MongoDB\BSON\toJSON(MongoDB\BSON\fromPHP($document))));
}
$alertMongo->printVar($posts);
/**/

/*Insertar datos
$bulk = new MongoDB\Driver\BulkWrite;
        $bulk->insert([
            "word" => 'Avianca',
            "active" => 'S',
            "fecha" => new \MongoDB\BSON\UTCDateTime()
            ]);
            $result = $mongo->executeBulkWrite('callaut.tweet', $bulk);
            if ($result->getInsertedCount() >= 1) {
                return true;
                
            } else {
                return false;
                
            }
*/
?>