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


document.addEventListener('mousemove', (event) => {
    const { clientX: mouseX, clientY: mouseY } = event;

    document.querySelectorAll('.pupil').forEach((pupil) => {
        // Получить координаты глаза относительно страницы
        const eyeRect = pupil.parentElement.getBoundingClientRect();

        // Вычислить разницу между центром глаза и положением мыши
        const deltaX = mouseX - (eyeRect.left + eyeRect.width / 2);
        const deltaY = mouseY - (eyeRect.top + eyeRect.height / 2);

        // Вычислить угол и расстояние от центра глаза до мыши
        const angle = Math.atan2(deltaY, deltaX);
        const distance = Math.min(eyeRect.width / 4, Math.sqrt(deltaX * deltaX + deltaY * deltaY));

        // Установить новую позицию зрачка
        const pupilX = distance * Math.cos(angle);
        const pupilY = distance * Math.sin(angle);
        pupil.style.transform = `translate(${pupilX}px, ${pupilY}px)`;
    });
});
