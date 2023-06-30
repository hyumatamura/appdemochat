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
import os

import logging 
import re

app = Flask(__name__)
#appをflaskのインスタンスとして作成

logging.basicConfig(level=logging.DEBUG)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["ACCESS"]
YOUR_CHANNEL_SECRET = os.environ["SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

x_value = 0
y_value = 0

@app.route("/callback", methods=['POST'])
def callback():
    logging.warning("hello")
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
def handle_message(event):
    message_text = event.message.text
    
    x_value = 100
    y_value = 100

    if '@tip' in message_text:
        if 'from@x' in message_text:
            amount = re.sub(r"\D", "", message_text)
            amount = int(amount)
            x_value = x_value - amount
            y_value = y_value + amount
            reply_text = f"xの残高は{x_value}です。yの残高は{y_value}です。"

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply_text)
            )
        
        elif 'from@y' in message_text:
            amount = re.sub(r"\D", "", message_text)
            amount = int(amount)
            x_value = x_value + amount
            y_value = y_value - amount
            reply_text = f"xの残高は{x_value}です。yの残高は{y_value}です。"

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply_text)
            )

        else :
            reply_text = f"xの残高は{x_value}です。yの残高は{y_value}です。"
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply_text)
            )
    else:
        pass


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

