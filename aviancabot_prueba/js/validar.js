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

});
});


$( document ).ready(function() {
    $("#excel").submit(function() {
		//alert("sdfsd");
		if($("#from").val() == ""){
			alert("Debe seleccionar la fecha inicial de la consulta.");	
			return false;
		}else if($("#to").val() == ""){
			alert("Debe seleccionar la fecha final de la consulta.");
			return false;	
		}else if($("#from").val() > $("#to").val()){
			alert("La fecha desde debe ser menor a la de hasta.");
			return false;	
		}
		
	});
});
