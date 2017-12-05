<?php  
require_once("class/classMongo.php");
require_once("class/php-export-data.class.php");

$fecha = date('Y-m-d H:i:s');
$excel = new ExportDataExcel('browser');
$excel->filename = $fecha."-tweet escalados.xls";


$from = $_REQUEST['from'];
$to = $_REQUEST['to'];

$Excel = new AlertMongo();
$datos = $Excel->excel($from,$to);
//echo $Excel->printVar($datos[0]->fecha);


	//$excel_obj = new ExportExcel($fecha."-personas registradas.xls");
	// Setting the values of the headers and data of the excel file
	// and these values comes from the other file which file shows the data
	$excelHeader = array(array(
		"IdTweet",
		"Followers",
		"Favorites",
		"Retweet",
		"Tweet",
		"Usuario creo tweet",
		"Fecha de tweet",
		"Link",
		"Tipo de alerta",
		"Fecha escalo",
		"Funcionario escalo"
	));
	
	if($datos){
	
		$excelValues = array();
		for( $i=0; $i < count($datos); $i++){
			if(isset($datos[$i]->idTweeet)){
				$excelValues[$i][]= $datos[$i]->idTweeet;
			}else{
				$excelValues[$i][] = "";
			}
			
			if(isset($datos[$i]->followers)){
				$excelValues[$i][]= $datos[$i]->followers;
			}else{
				$excelValues[$i][] = "";
			}

			if(isset($datos[$i]->favorite)){
				$excelValues[$i][]= $datos[$i]->favorite;
			}else{
				$excelValues[$i][] = "";
			}

			if(isset($datos[$i]->retweet)){
				$excelValues[$i][]= $datos[$i]->retweet;
			}else{
				$excelValues[$i][] = "";
			}

			if(isset($datos[$i]->tweet)){
				$excelValues[$i][]= $datos[$i]->tweet;
			}else{
				$excelValues[$i][] = "";
			}

			if(isset($datos[$i]->usuario)){
				$excelValues[$i][]= $datos[$i]->usuario;
			}else{
				$excelValues[$i][] = "";
			}

			if(isset($datos[$i]->fechaTweet)){
				$excelValues[$i][]= $datos[$i]->fechaTweet;
			}else{
				$excelValues[$i][] = "";
			}

			if(isset($datos[$i]->link)){
				$excelValues[$i][]= $datos[$i]->link;
			}else{
				$excelValues[$i][] = "";
			}

			if(isset($datos[$i]->tipoAlerta)){
				$excelValues[$i][]= $datos[$i]->tipoAlerta;
			}else{
				$excelValues[$i][] = "";
			}
					
			if(isset($datos[$i]->fechaCol)){
				$excelValues[$i][] = $datos[$i]->fechaCol;
			}else{
				$excelValues[$i][] = "";
			}

			if(isset($datos[$i]->UserReport)){
				$excelValues[$i][] = $datos[$i]->UserReport;
			}else{
				$excelValues[$i][] = "";
			}
	
		}
	
		$excel->initialize();
	
		foreach($excelHeader as $row) {
			$excel->addRow($row);
		}
	
		foreach($excelValues as $row) {
			$excel->addRow($row);
		}
	
		$excel->finalize();

	}else{
		echo "Para el rango de fechas del ".$from." hasta el ".$to." no existe información.";
	}
//}

/*
$from = $_REQUEST['from'];
$to = $_REQUEST['to'];

echo $from."   ".$to;

$Excel = new AlertMongo();
$resultado = $Excel->excel($from,$to);
echo $Excel->printVar($resultado);
*/
//echo $resultado[0]->tipoAlerta;
?>
