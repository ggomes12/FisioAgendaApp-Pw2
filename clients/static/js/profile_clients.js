$(function() {
    $("#dataConsulta").datepicker({
        dateFormat: 'dd/mm/yy',
        minDate: 0, 
        onSelect: function(dateText) {
            // logica
            console.log("Data selecionada: " + dateText);
        }
    });
});
