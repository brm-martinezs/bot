<?php
//ini_set('display_errors', 1);
//error_reporting(E_ALL);
require_once('class/TwitterAPIExchange.php');
require('class/classMongo.php');
//date_default_timezone_set('America/Bogota');

$alertMongo= new AlertMongo();

$busqueda=$alertMongo->getTWord();
$queryS=array();
foreach($busqueda as $key => $value){
    //printVar($value->word);
    array_push($queryS,strtolower($value->word));
}
$queryF=implode(' OR ',$queryS);




/** Set access tokens here - see: https://dev.twitter.com/apps/ **/
$settings = array(
    'oauth_access_token' => "782779396675477504-q8wnkKCQVcWVVJ2IqLxMxWGTi7aYWJD",
    'oauth_access_token_secret' => "WHYKEgHORfhEfHD4LgPM4LDgCbtEbUJTKwZCn8GQOQp1x",
    'consumer_key' => "DwDK8z8hhd1VBWToqKkEWraeN",
    'consumer_secret' => "QfFQ8HNGdFWZYphVu62Bsx6JtDA72FPA1onXZkYa5WQxJexi2V"
);
$idLastTweet=$alertMongo->getLastIdTweet();

//$alertMongo->printVar($idLastTweet);
//$alertMongo->printVar($idLastTweet[0]->_id->__toString(),'id');
//$alertMongo->printVar($idLastTweet[0]->fecha->$date,'fecha');

if(!empty($idLastTweet)){
    //$alertMongo->printVar($idLastTweet);
    $campos['id']=$idLastTweet[0]['id'];
    $campos['fecha']=$idLastTweet[0]['fecha'];
    $campos['cuentaInsert']=$idLastTweet[0]['contador'];
    $insertLast=$alertMongo->insertLastTweetSend($campos);
    $contador=(int)$idLastTweet[0]['contador']+1;
}else{
    $contador=1;
}

//$alertMongo->printVar($contador,'conteo');
//die();         


$url = 'https://api.twitter.com/1.1/search/tweets.json';
/*Acá en esta linea toca mandarle el nextId para que traiga los tweets después del último traido*/
//$getfield = '?q='.$queryF.'&l=es&src=typd';
$getfield = '?q=Avianca AND '.$destino;
//printVar($getfield);
//die();
$requestMethod = 'GET';

$twitter = new TwitterAPIExchange($settings);
$response = $twitter->setGetfield($getfield)
    ->buildOauth($url, $requestMethod)
    ->performRequest();

$responseJ=json_decode($response);
$guardaT= array();
//$alertMongo->printVar($responseJ->statuses);
//die();
$conteoTW=count($responseJ->statuses);
$tweet=$responseJ->statuses;
for($i=0; $i<$conteoTW;$i++){
    $campos['textoTw']=$tweet[$i]->text;
    $campos['idText']=$tweet[$i]->id_str;
    $campos['fechaText']=$tweet[$i]->created_at;
    $campos['idTw']=$tweet[$i]->user->id_str;
    $campos['arroa']=$tweet[$i]->user->screen_name;
    $campos['followers']=$tweet[$i]->user->followers_count;
    $campos['retweet']=$tweet[$i]->retweet_count;
    $campos['favorite']=$tweet[$i]->favorite_count;
    $traeTweet=$alertMongo->getTweet($campos['idText']);
    if(empty($traeTweet)){
        $campos['cuentaInsert']=$contador;
        $result=$alertMongo->insertTweet($campos);
        $contador=$contador+1;
        $alertMongo->printVar($result,"Guarda");
        echo $tweet[$i]->text;
    }else{
        $alertMongo->printVar("Ya existe");
    }
}