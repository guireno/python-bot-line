# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('28JYp0m8fuIWAwLIsb5XkDAwLH4F80DhhYRMLeu8JG659TMDvM4zTo9T1aq9lLxVqOi7F+uuoJZT2xvX6D5xpfHQVqkk8Uoir9KSXAtR6gZEoiKayATHDha2+bK95BsSoJA8OuKyqdraSuBCVN3Z1AdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('08627db7ed5696c79b242c184905b6ef') #Your Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
