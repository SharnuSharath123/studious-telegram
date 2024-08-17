from flask import Flask, request, jsonify
from telegram import Bot

app = Flask(__name__)
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
bot = Bot(token=TELEGRAM_TOKEN)

@app.route('/')
def home():
    return "Welcome to the Telegram Bot App!"

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    chat_id = data.get('chat_id')
    message = data.get('message')
    
    if chat_id and message:
        bot.send_message(chat_id=chat_id, text=message)
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Chat ID or message missing'}), 400

if __name__ == '__main__':
    app.run(debug=True)
