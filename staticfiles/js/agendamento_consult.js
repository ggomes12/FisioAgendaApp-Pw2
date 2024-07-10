document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("consultaForm");
    const dataInput = form.querySelector("#id_data");
    const horarioInicialInput = form.querySelector("#id_horario_inicial");
    const horarioFinalInput = form.querySelector("#id_horario_final");

    dataInput.addEventListener("change", function() {
        const dataSelecionada = dataInput.value;
        const horarioInicial = horarioInicialInput.value;
        const horarioFinal = horarioFinalInput.value;

        if (horarioInicial && horarioFinal) {
            const url = `/clients/unavailable_dates/${profissional_id}/?data=${dataSelecionada}&horario_inicial=${horarioInicial}&horario_final=${horarioFinal}`;

            $.ajax({
                url: url,
                success: function(response) {
                    console.log(response); // Verificar a resposta JSON para ajustes
                    disableUnavailableDates(response.unavailable_dates);
                },
                error: function(xhr, errmsg, err) {
                    console.error(xhr.status + ": " + xhr.responseText);
                    // Implementar lógica de tratamento de erro, se necessário
                }
            });
        }
    });

    function disableUnavailableDates(unavailableDates) {
        // Habilitar todos os dias
        const allDates = document.querySelectorAll('.datepicker tbody td');
        allDates.forEach(function(date) {
            date.classList.remove('unavailable');
            date.style.pointerEvents = 'auto'; // Garante que os dias sejam clicáveis
        });

        // Desabilitar os dias indisponíveis
        unavailableDates.forEach(function(dateStr) {
            const date = new Date(dateStr);
            const year = date.getFullYear();
            const month = date.getMonth() + 1; // JavaScript usa 0 para janeiro
            const day = date.getDate();
            const formattedDate = `${year}-${month}-${day}`;

            const selector = `.datepicker tbody td[data-date="${formattedDate}"]`;
            const disabledDate = document.querySelector(selector);
            if (disabledDate) {
                disabledDate.classList.add('unavailable');
                disabledDate.style.pointerEvents = 'none'; // Impede cliques nos dias indisponíveis
            }
        });
    }
});
