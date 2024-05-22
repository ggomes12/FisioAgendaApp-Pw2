$(function() {
    $("#detalhesClienteDialog").dialog({
        autoOpen: false,
        modal: true,
    });

    $(".dia-agendado").css("background-color", "red");

    $(".dia-agendado").click(function() {
        const dataAgendada = $(this).data("date");
        const nomeCliente = $(this).data("cliente");

        $("#nomeCliente").text("Cliente: " + nomeCliente);
        $("#dataAgendada").text("Data Agendada: " + dataAgendada);

        $(".dia-agendado").removeClass("clicado");
        $(this).addClass("clicado");

        $("#detalhesClienteDialog").dialog("open");
    });


    $(".concluir-agendamento-dialog").click(function() {

        $("#detalhesClienteDialog").dialog("close");


        $(".dia-agendado.clicado").css("background-color", "green");
    });
});
