import os
from datetime import datetime
import json
from flask import Flask, abort, request

from linebot.models import *
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token, ImagemapSendMessage(json.load(open('imagemap_1.json', 'r', encoding='utf-8'))))
    
    msg = event.message.text 
    if(msg == 'temp1'):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text = '測試',
                contents = json.load(open('temp1.json', 'r', encoding='utf-8'))
            )
        )
    elif(msg == 'temp2'):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text = '測試',
                contents = json.load(open('temp2.json', 'r', encoding='utf-8'))
            )
        )

    else:
        # quick reply
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(
        text="文字訊息",
        quick_reply=QuickReply(
            items=[
                    QuickReplyButton(
                        image_url="https://cdn-icons-png.flaticon.com/128/3917/3917261.png",
                        action=MessageAction(label="詢問出團日期",text="詢問出團日期")
                        ),
                    QuickReplyButton(
                        image_url="https://cdn-icons-png.flaticon.com/128/3917/3917261.png",
                        action=MessageAction(label="詢問出團日期",text="詢問出團日期")
                        ),
                    QuickReplyButton(
                        action=MessageAction(label="成團資訊",text="成團資訊")
                        )

                    ]
                )
            )
        )
        # return line_bot_api.replyMessage(event.replyToken,json.load(open('temp2.json', 'r', encoding='utf-8')))
        
        # get_message = event.message.text
        # # Send To Line
        # reply = TextSendMessage(text=f"{get_message}")
        # line_bot_api.reply_message(event.reply_token, reply)

