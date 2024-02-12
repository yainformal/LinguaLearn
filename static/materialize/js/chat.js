// chat.js
const chatSocket = new WebSocket('{{ websocket_url }}');

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
    chatSocket.send(JSON.stringify({
        'message': message,
        'sender': 'user'
    }));
}

function addUserMessage(message) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('user-message');
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
}

function addBotMessage(message) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('bot-message');
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
}

document.getElementById('message-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const userMessageInput = document.getElementById('user_message');
    const userMessage = userMessageInput.value;
    userMessageInput.value = '';
    addUserMessage(userMessage);
    sendMessageToBot(userMessage);
});
