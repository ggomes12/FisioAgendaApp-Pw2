    // Função para exibir a modal com a mensagem
    function showMessage(message) {
        var modal = document.getElementById('messageModal');
    var modalMessage = document.getElementById('modalMessage');
    modalMessage.innerText = message;
    modal.style.display = 'block';
    }

    // Fechar a modal ao clicar no botão de fechar
    document.getElementsByClassName('close')[0].addEventListener('click', function() {
        var modal = document.getElementById('messageModal');
    modal.style.display = 'none';
    });

    // Fechar a modal ao clicar fora dela
    window.addEventListener('click', function(event) {
        var modal = document.getElementById('messageModal');
    if (event.target == modal) {
        modal.style.display = 'none';
        }
    });