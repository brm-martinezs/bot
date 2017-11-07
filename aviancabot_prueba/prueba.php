<?php  
$texto = "RT @Avianca no me responde por una cancelacion que yo no hice pero tampoco me resuelve mi estadía ni regreso #abusivos";
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