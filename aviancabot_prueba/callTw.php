<?php

/*Función para hacer depuración del código*/
    function printVar( $variable, $title = "" ){
        $var = print_r( $variable, true );
        echo "<pre style='background-color:#dddd00; border: dashed thin #000000;'><strong>[$title]</strong> $var</pre>";
    }

ini_set('display_errors', 1);
error_reporting(E_ALL);
require_once('class/TwitterAPIExchange.php');

/** Set access tokens here - see: https://dev.twitter.com/apps/ **/
$settings = array(
    'oauth_access_token' => "1511544307-UZY4gBRAjk6XVwA9fwLbQNL0OjerLilyUMroISQ",
    'oauth_access_token_secret' => "be14M1AcX8m0XtlLQlbIzHEaPKpmpVwFgPGXnCVbMmqMX",
    'consumer_key' => "VZFc09NThPlXQiaZBMMOxc3qX",
    'consumer_secret' => "iN1y927KrLtjbLVh9gpCymB4w78meP9g22D0l6npmB2i7WsX65"
);


//$alertMongo->printVar($contador,'conteo');
//die();         


$url = 'https://api.twitter.com/1.1/statuses/user_timeline.json';
/*Acá en esta linea toca mandarle el nextId para que traiga los tweets después del último traido*/
//$getfield = '?q='.$queryF.'&l=es&src=typd';
$getfield = '?screen_name=faquima24&count=100';
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

echo printVar($responseJ);

?>