<?php  
$texto = "RT @gacv1985: @Avianca  estoy en el aeropuerto de santa Marta y me dicen que mi tiquete fue reembolsado y que no puedo viajar, yo nunca sol…";
for($i=0;$i<2;$i++)
{	$primerLetra = $texto[0];
	$segundaLetra = $texto[1];
}
$esRetweet = $primerLetra.$segundaLetra;
if($esRetweet == 'RT'){
	echo "Es RT";
}else{
	echo "No es RT";
}
?>