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

room_data = {}

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

@app.route("/test", methods=["GET"])
def test():
    logging.warning("hello")
    return "ok"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = event.message.text
    
    if '@mention' in message_text:
        reply_text = "あいうえお"
    else:
        reply_text = "数字を入力してください。"
            
    line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply_text)
            )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

