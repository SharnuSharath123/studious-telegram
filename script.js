document.getElementById('messageForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const chatId = document.getElementById('chatId').value;
    const message = document.getElementById('message').value;

    fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ chat_id: chatId, message: message })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseMessage').textContent = data.status === 'success' ? 'Message sent successfully!' : 'Error: ' + data.message;
    })
    .catch(error => {
        document.getElementById('responseMessage').textContent = 'Error: ' + error.message;
    });
});
