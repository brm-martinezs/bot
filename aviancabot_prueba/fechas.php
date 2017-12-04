<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<title>jQuery UI Datepicker - Seleccionar un rango de fechas</title>
<link rel="stylesheet" href="http://code.jquery.com/ui/1.10.1/themes/base/jquery-ui.css" />
<script src="http://code.jquery.com/jquery-1.9.1.js"></script>
<script src="http://code.jquery.com/ui/1.10.1/jquery-ui.js"></script>


<script>

jQuery(function($){
   $.datepicker.regional['es'] = {
      closeText: 'Cerrar',
      prevText: '<Ant',
      nextText: 'Sig>',
      currentText: 'Hoy',
      monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
      monthNamesShort: ['Ene','Feb','Mar','Abr', 'May','Jun','Jul','Ago','Sep', 'Oct','Nov','Dic'],
      dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
      dayNamesShort: ['Dom','Lun','Mar','Mié','Juv','Vie','Sáb'],
      dayNamesMin: ['Do','Lu','Ma','Mi','Ju','Vi','Sá'],
      weekHeader: 'Sm',
      dateFormat: 'yy-mm-dd',
      firstDay: 1,
      isRTL: false,
      showMonthAfterYear: false,
      yearSuffix: ''};
   $.datepicker.setDefaults($.datepicker.regional['es']);
});

$(function () {
$("#from").datepicker({
maxDate : "0",
onClose: function (selectedDate) {
$("#to").datepicker("option", "minDate", selectedDate);
}
});
});

$(function () {
$("#to").datepicker({
maxDate : "0",
onClose: function (selectedDate) {
$("#from").datepicker("option", "maxDate", selectedDate);
}
});
});


$( document ).ready(function() {
    $("#excel").submit(function() {
		//alert("sdfsd");
		if($("#from").val() == ""){
			alert("Debe seleccionar la fecha inicial de la consulta");	
			return false;
		}else if($("#to").val() == ""){
			alert("Debe seleccionar la fecha final de la consulta");
			return false;	
		}
		
	});
});


</script>

</head>

<body>
<form name="excel" id="excel" method="post" action="generarExcel.php" target="_blank">
<p>
Fechas 
Desde:
<input type="text" id="from" name="from" />
Hasta:
<input type="text" id="to" name="to" />

<input type="submit" name="consultar" value="Consultar">
</p>
</form>
<div id="mensaje">
	
</div>
</body>
</html>