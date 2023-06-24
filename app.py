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

    elif(msg == 'quick'):
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
    elif(msg == 'map'):
        # imagemap
        # imagemap_message = ImagemapSendMessage(
        # base_url='https://github.com/keit1216/Flask-LINE-Bot-Heroku-main/tree/main/switzerland',
        # alt_text='this is an imagemap',
        # base_size=BaseSize(height=1830, width=1040),
        # actions=[
        #     URIImagemapAction(
        #         link_uri='https://switzerland-travel.tw/travel/eighteen/',
        #         area=ImagemapArea(
        #             x=19, y=601, width=492, height=366
        #         )
        #     ),
        #     URIImagemapAction(
        #         link_uri='https://switzerland-travel.tw/travel/【純瑞旅遊10日】收錄少女峰馬特宏峰白朗峰黃金/',
        #         area=ImagemapArea(
        #             x=529, y=600, width=492, height=369
        #         )
        #     ),
        #     URIImagemapAction(
        #         link_uri='https://switzerland-travel.tw/travel/germany-switzerland-10days/',
        #         area=ImagemapArea(
        #             x=19, y=995, width=494, height=369
        #         )
        #     ),
        #     URIImagemapAction(
        #         link_uri='https://switzerland-travel.tw/travel/10-days-in-switzerland/',
        #         area=ImagemapArea(
        #             x=527, y=997, width=496, height=364
        #         )
        #     ),
        #     URIImagemapAction(
        #         link_uri='https://switzerland-travel.tw/travel/br-milan-10days/',
        #         area=ImagemapArea(
        #             x=16, y=1394, width=497, height=361
        #         )
        #     ),
        #     URIImagemapAction(
        #         link_uri='https://switzerland-travel.tw/travel/10-days-in-switzerland-2/',
        #         area=ImagemapArea(
        #             x=529, y=1392, width=492, height=373
        #         )
        #     )
        # ]
        # )
        # line_bot_api.reply_message(event.reply_token, imagemap_message)

        # imagemap
        imagemap_message = ImagemapSendMessage(
        base_url='https://github.com/line/line-bot-sdk-nodejs/raw/master/examples/kitchensink/static/rich',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            URIImagemapAction(
                link_uri='https://google.com/',
                area=ImagemapArea(
                    x=0, y=586, width=520, height=454
                )
            ),
            MessageImagemapAction(
                text='hello',
                area=ImagemapArea(
                    x=520, y=586, width=520, height=454
                )
            )
        ]
        )
        line_bot_api.reply_message(event.reply_token, imagemap_message)

    elif ('出團資訊' in msg):
        line_bot_api.reply_message(
            event.reply_token,
            ImagemapSendMessage(
                alt_text = 'test',
                contents = json.load(open('travel_info.json', 'r', encoding='utf-8'))
            )
        )
        # get_message = event.message.text
        # # Send To Line
        # reply = TextSendMessage(text=f"{get_message}")
        # line_bot_api.reply_message(event.reply_token, reply)

