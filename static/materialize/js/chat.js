// Инициализация WebSocket соединения
//const chatSocket = new WebSocket('ws://localhost:8000/ws/chat/');

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const message = data.message;
    const sender = data.sender;
    if (sender === 'user') {
        addUserMessage(message);
    } else if (sender === 'bot') {
        addBotMessage(message);
    }
};

function sendMessageToBot(message) {
    if (chatSocket.readyState === WebSocket.OPEN) {
        chatSocket.send(JSON.stringify({
            'message': message,
            'sender': 'user'
        }));
    } else {
        console.error("WebSocket соединение не открыто.");
    }
}


function addUserMessage(message) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('user-message');
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight; // Автопрокрутка к последнему сообщению
}

function addBotMessage(message) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('bot-message');
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight; // Автопрокрутка к последнему сообщению
}

document.getElementById('message-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const userMessageInput = document.getElementById('user_message');
    const userMessage = userMessageInput.value.trim(); // Удаление лишних пробелов
    if (userMessage !== '') { // Проверка на пустое сообщение
        addUserMessage(userMessage);
        sendMessageToBot(userMessage);
        userMessageInput.value = ''; // Очистка поля ввода после отправки
    }
});
