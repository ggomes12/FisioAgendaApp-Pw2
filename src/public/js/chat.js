document.addEventListener('DOMContentLoaded', function() {
    const chatBody = document.getElementById('chatBody');
    const messageInput = document.getElementById('messageInput');
    const sendMessageBtn = document.getElementById('sendMessage');

    sendMessageBtn.addEventListener('click', function() {
        const messageText = messageInput.value.trim();

        if (messageText !== '') {
            appendMessage(messageText, 'sent');
            messageInput.value = '';
        }
    });

    function appendMessage(text, className) {
        const message = document.createElement('div');
        message.className = 'message ' + className;
        message.textContent = text;
        chatBody.appendChild(message);

        chatBody.scrollTop = chatBody.scrollHeight;
    }
});
