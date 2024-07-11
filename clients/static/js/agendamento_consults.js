$(document).ready(function() {
    // Verifica se o JSON dos dias indisponíveis foi carregado corretamente
    if (typeof diasIndisponiveis === 'undefined') {
        console.error("diasIndisponiveis não está definido.");
        return;
    }

    // Inicializa o calendário jQuery UI
    $('#id_data').datepicker({
        dateFormat: 'yy-mm-dd',  // Formato da data
        minDate: 0,  // A partir de hoje
        beforeShowDay: function(date) {
            // Formata a data para 'yyyy-mm-dd'
            var formattedDate = $.datepicker.formatDate('yy-mm-dd', date);
            
            // Verifica se a data está nas datas disponíveis
            if (diasIndisponiveis.includes(formattedDate)) {
                return [false, "", "Indisponível"];
            } else {
                return [true, "", ""];
            }
        }
    });
});
