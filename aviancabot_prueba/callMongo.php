<?php

ini_set('display_errors', 1);
require('class/classMongo.php');
$alertMongo= new AlertMongo();


/*$lastTweet=$alertMongo->searhLastIdTweet();

if(!empty($lastTweet)){
    $lastSend=$lastTweet[0]['lastSend'];
}else{
    $lastSend=0;
}*/

//$alertMongo->printVar($lastSend);
//die();

$concidencias=array('avianca','Avianca',"@Avianca");
$almacen=array();
foreach ($concidencias as $key => $value) {
    
    $result=$alertMongo->getTweetMongo($value);
    $count=count($result);
    for ($i=0;$i<$count;$i++){

        array_push($almacen,$result[$i]);
        $actualizaTweet=$alertMongo->updateTweetSend($result[$i]->idText);

        
    }
    
}

$alertMongo2 = new AlertMongo();
$palabras = $alertMongo2->getPalabras();
foreach ($almacen as $key=>$val ){
 
  	$esta = 0;
	
	for($i=0;$i<count($palabras);$i++){
		$posicion_coincidencia = strpos($val->texto, $palabras[$i]);	
		//se puede hacer la comparacion con 'false' o 'true' y los comparadores '===' o '!=='
		if ($posicion_coincidencia === false){
	    }else{
	        $esta ++;
	    }
	}
 
	if($esta != 0){
		echo "idTweet:$val->idText ~|~ @$val->arrobaUsuario | Followers $val->followers | Favs $val->favorite | Retweets $val->retweet | Tweet $val->texto"."°";
	}else{
	}
}