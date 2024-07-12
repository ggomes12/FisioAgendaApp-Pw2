$(document).ready(function() {
    $('#id_data').datepicker({
        dateFormat: 'yy-mm-dd',
        minDate: 0,
        beforeShowDay: function(date) {
            var formattedDate = $.datepicker.formatDate('yy-mm-dd', date);
            var isDisponivel = true;

            // Captura os horários atuais do cliente
            var horarioInicialCliente = $('#id_horario_inicial').val();
            var horarioFinalCliente = $('#id_horario_final').val();

            // Verifica se a data está na lista de dias indisponíveis
            if (diasIndisponiveis.includes(formattedDate)) {
                // Captura consultas para esta data específica
                var consultasParaData = consultas.filter(function(consulta) {
                    return consulta.data === formattedDate;
                });

                // Verifica se há sobreposição de horários
                consultasParaData.forEach(function(consulta) {
                    var consultaInicio = consulta.horario_inicial;
                    var consultaFim = consulta.horario_final;

                    // Converte horários para formato adequado para comparação (HH:MM)
                    var horarioInicialConsulta = ('0' + consultaInicio.getHours()).slice(-2) + ':' + ('0' + consultaInicio.getMinutes()).slice(-2);
                    var horarioFinalConsulta = ('0' + consultaFim.getHours()).slice(-2) + ':' + ('0' + consultaFim.getMinutes()).slice(-2);

                    // Verifica se há sobreposição com o horário informado pelo cliente
                    if (!(horarioFinalCliente <= horarioInicialConsulta || horarioFinalConsulta <= horarioInicialCliente)) {
                        isDisponivel = false;
                        return false;  // Para o loop forEach
                    }
                });
            }

            // Retorna array com disponibilidade do dia
            if (isDisponivel) {
                return [true, "", ""];
            } else {
                return [false, "", "Indisponível"];
            }
        }
    });
});
