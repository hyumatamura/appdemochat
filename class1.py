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

a_value = 0 
#Hyuma
b_value = 0
#Daisuke
c_value = 0
#Hitomi
d_value = 0
#Chihaya
e_value = 0
#Yoshida
f_value = 0
#Rioko

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    global a_value
    global b_value
    global c_value
    global d_value
    global e_value
    global f_value
    
    message_text = event.message.text

    if '@tip' in message_text:
        if 'from@Hyuma' in message_text:
            if "to@Daisuke" in message_text: 
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                a_value = a_value - amount
                b_value = b_value + amount
                reply_text = f"Hyumaのチャミスル残高は{a_value}です。Daisukeのチャミスル残高は{b_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )
            
            elif "to@Hitomi" in message_text:
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                a_value = a_value - amount
                c_value = c_value + amount
                reply_text = f"Hyumaのチャミスル残高は{a_value}です。Hitomiのチャミスル残高は{c_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )
            
            elif "to@Chihaya" in message_text:
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                a_value = a_value - amount
                d_value = d_value + amount
                reply_text = f"Hyumaのチャミスル残高は{a_value}です。Chihayaのチャミスル残高は{d_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )
            
            elif "to@Yoshida" in message_text:
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                a_value = a_value - amount
                e_value = e_value + amount
                reply_text = f"Hyumaのチャミスル残高は{a_value}です。Yoshidaのチャミスル残高は{e_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )

            
            elif "to@Rioko" in message_text:
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                a_value = a_value - amount
                f_value = f_value + amount
                reply_text = f"Hyumaのチャミスル残高は{a_value}です。Riokoのチャミスル残高は{f_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )
                
            else : 
                reply_text = f"Hyumaさん、正しいフォーマットで入力して下さい。 @tip from@Hyuma to@誰か"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )
            
        
        elif 'from@Daisuke' in message_text:
            if "to@Hyuma" in message_text: 
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                b_value = b_value - amount
                a_value = a_value + amount
                reply_text = f"Hyumaのチャミスル残高は{a_value}です。Daisukeのチャミスル残高は{b_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )
            
            elif "to@Hitomi" in message_text:
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                b_value = b_value - amount
                c_value = c_value + amount
                reply_text = f"Daisukeのチャミスル残高は{b_value}です。Hitomiのチャミスル残高は{c_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )
            
            elif "to@Chihaya" in message_text:
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                b_value = b_value - amount
                d_value = d_value + amount
                reply_text = f"Daisukeのチャミスル残高は{b_value}です。Chihayaのチャミスル残高は{d_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )
            
            elif "to@Yoshida" in message_text:
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                b_value = b_value - amount
                e_value = e_value + amount
                reply_text = f"Daisukeのチャミスル残高は{b_value}です。Yoshidaのチャミスル残高は{e_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )

            
            elif "to@Rioko" in message_text:
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                b_value = b_value - amount
                f_value = f_value + amount
                reply_text = f"Daisukeのチャミスル残高は{b_value}です。Riokoのチャミスル残高は{f_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )
                
            else : 
                reply_text = f"Daisukeさん、正しいフォーマットで入力して下さい。 @tip from@Daisuke to@誰か"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )
        
        elif 'from@Hitomi' in message_text:
            if "to@Hyuma" in message_text: 
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                c_value = c_value - amount
                a_value = a_value + amount
                reply_text = f"Hyumaのチャミスル残高は{a_value}です。Hitomiのチャミスル残高は{c_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )
            
            elif "to@Daisuke" in message_text:
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                c_value = c_value - amount
                b_value = b_value + amount
                reply_text = f"Daisukeのチャミスル残高は{b_value}です。Hitomiのチャミスル残高は{c_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )
            
            elif "to@Chihaya" in message_text:
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                c_value = c_value - amount
                d_value = d_value + amount
                reply_text = f"Hitomiのチャミスル残高は{c_value}です。Chihayaのチャミスル残高は{d_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )
            
            elif "to@Yoshida" in message_text:
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                c_value = c_value - amount
                e_value = e_value + amount
                reply_text = f"Hitomiのチャミスル残高は{c_value}です。Yoshidaのチャミスル残高は{e_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )

            
            elif "to@Rioko" in message_text:
                amount = re.sub(r"\D", "", message_text)
                amount = int(amount)
                c_value = c_value - amount
                f_value = f_value + amount
                reply_text = f"Hitomiのチャミスル残高は{c_value}です。Riokoのチャミスル残高は{f_value}です。"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )
                
            else : 
                reply_text = f"Hitomiさん、正しいフォーマットで入力して下さい。 @tip from@Daisuke to@誰か"

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=reply_text)
                 )

        else :
            reply_text = f"チャミスル残高は以下の通りです。Hyuma={a_value}。Daisuke={b_value}。 Hitomi={c_value}。 Chihaya={d_value}。 Yoshida={e_value}。Rioko={f_value}"
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply_text)
            )
    else:
        pass


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

