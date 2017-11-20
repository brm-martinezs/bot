<?php  

/*Función para hacer depuración del código*/
    function printVar( $variable, $title = "" ){
        $var = print_r( $variable, true );
        echo "<pre style='background-color:#dddd00; border: dashed thin #000000;'><strong>[$title]</strong> $var</pre>";
    }

require_once('TwitterAPIExchange.php');

$settings = array(
    'oauth_access_token' => "782779396675477504-q8wnkKCQVcWVVJ2IqLxMxWGTi7aYWJD",
    'oauth_access_token_secret' => "WHYKEgHORfhEfHD4LgPM4LDgCbtEbUJTKwZCn8GQOQp1x",
    'consumer_key' => "DwDK8z8hhd1VBWToqKkEWraeN",
    'consumer_secret' => "QfFQ8HNGdFWZYphVu62Bsx6JtDA72FPA1onXZkYa5WQxJexi2V"
);

$url = 'https://api.twitter.com/1.1/statuses/user_timeline.json';
$getfield = '?screen_name=patriperezg&count=15';        
$requestMethod = 'GET';
$twitter = new TwitterAPIExchange($settings);
$json =  $twitter->setGetfield($getfield)
                     ->buildOauth($url, $requestMethod)
                     ->performRequest();
printVar(json_decode($json));

?>