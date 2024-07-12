$(document).ready(function() {
    // Verifica se o JSON dos dias indisponíveis foi carregado corretamente
    if (typeof diasIndisponiveis === 'undefined') {
        console.error("diasIndisponiveis não está definido.");
        return;
    }

    // Inicializa o datepicker no campo de data
    $('#id_data').datepicker({
        dateFormat: 'yy-mm-dd', 
        minDate: 0, 
        beforeShowDay: function(date) {
            var formattedDate = $.datepicker.formatDate('yy-mm-dd', date);
            if (diasIndisponiveis.includes(formattedDate)) {
                return [false, "", "Indisponível"];
            } else {
                return [true, "", ""];
            }
        }
    });
});