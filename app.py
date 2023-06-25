import os
from datetime import datetime
import json
from flask import Flask, abort, request

from linebot.models import *
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FollowEvent


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
        imagemap_message = ImagemapSendMessage(
        base_url='https://res.cloudinary.com/dljndh8rq/image/upload/v1687509072/travelinfo',
        alt_text='索取出團資訊',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            MessageImagemapAction(
                text='索取13天行程資訊',
                area=ImagemapArea(
                    x=0, y=105, width=519, height=416
                )
            ),
            MessageImagemapAction(
                text='索取15天行程資訊',
                area=ImagemapArea(
                    x=520, y=106, width=520, height=414
                )
            ),
            MessageImagemapAction(
                text='索取18天行程資訊',
                area=ImagemapArea(
                    x=1, y=524, width=519, height=516
                )
            ),
            MessageImagemapAction(
                text='索取獨立成團資訊',
                area=ImagemapArea(
                    x=524, y=521, width=515, height=519
                )
            )
        ]
        )
        line_bot_api.reply_message(event.reply_token, imagemap_message)
    
    elif ('按鈕3' in msg):
        imagemap_message = ImagemapSendMessage(
        base_url='https://res.cloudinary.com/dljndh8rq/image/upload/v1687509135/3btn',
        alt_text='按鈕3',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            MessageImagemapAction(
                text='索取行程資訊',
                area=ImagemapArea(
                    x=104, y=184, width=394, height=362
                )
            ),
            MessageImagemapAction(
                text='索取出團日期',
                area=ImagemapArea(
                    x=543, y=182, width=392, height=365
                )
            ),
            MessageImagemapAction(
                text='專人諮詢',
                area=ImagemapArea(
                    x=103, y=576, width=836, height=317
                )
            )
        ]
        )
        line_bot_api.reply_message(event.reply_token, imagemap_message)

    elif(msg == '開始'):
        message_list = [
            TextSendMessage(text='你好 xxxx'),
            TextSendMessage(text='顯示圖片 我們擁有15年經驗'),
            ImagemapSendMessage(
                base_url='https://res.cloudinary.com/dljndh8rq/image/upload/v1687509072/travelinfo',
                alt_text='索取出團資訊',
                base_size=BaseSize(height=1040, width=1040),
                actions=[
                    MessageImagemapAction(
                        text='索取13天行程資訊',
                        area=ImagemapArea(
                            x=0, y=105, width=519, height=416
                        )
                    ),
                    MessageImagemapAction(
                        text='索取15天行程資訊',
                        area=ImagemapArea(
                            x=520, y=106, width=520, height=414
                        )
                    ),
                    MessageImagemapAction(
                        text='索取18天行程資訊',
                        area=ImagemapArea(
                            x=1, y=524, width=519, height=516
                        )
                    ),
                    MessageImagemapAction(
                        text='索取獨立成團資訊',
                        area=ImagemapArea(
                            x=524, y=521, width=515, height=519
                        )
                    )
                ]
            )
        ]
        line_bot_api.reply_message(event.reply_token, message_list)

        # get_message = event.message.text
        # # Send To Line
        # reply = TextSendMessage(text=f"{get_message}")
        # line_bot_api.reply_message(event.reply_token, reply)

@handler.add(PostbackEvent)
def handle_postback(event):
    postback_data = event.postback.data
    if ('出團資訊' in postback_data):
        imagemap_message = ImagemapSendMessage(
        base_url='https://res.cloudinary.com/dljndh8rq/image/upload/v1687509072/travelinfo',
        alt_text='索取出團資訊',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            MessageImagemapAction(
                text='索取13天行程資訊',
                area=ImagemapArea(
                    x=0, y=105, width=519, height=416
                )
            ),
            MessageImagemapAction(
                text='索取15天行程資訊',
                area=ImagemapArea(
                    x=520, y=106, width=520, height=414
                )
            ),
            MessageImagemapAction(
                text='索取18天行程資訊',
                area=ImagemapArea(
                    x=1, y=524, width=519, height=516
                )
            ),
            MessageImagemapAction(
                text='索取獨立成團資訊',
                area=ImagemapArea(
                    x=524, y=521, width=515, height=519
                )
            )
        ]
        )
    line_bot_api.reply_message(event.reply_token, imagemap_message)

@handler.add(FollowEvent)
def handle_follow(event):
    message_list = [
    TextSendMessage(text='菩提邦創辦人有15年的印度朝聖經驗\n \
                        服務超過2000海內外法友前往印度朝聖\n \
                        菩提邦印度朝聖的宗旨是\n \
                        「用心做好每一團 利益所有朝聖者」\n\
                        所以\n\
                        我們一台車45人座 只收20位\n\
                        我們一團20位法友\n\
                        由領隊導遊導遊助理三人服務\n\
                        為了讓所有參團的法友能夠有收穫，\n\
                        我們每個月都會舉辦兩場說明會\n\
                        一場是「如何擁有一次殊勝難得的朝聖因緣」\n\
                        另一場則是「聖地與經典」\n\
                        希望透過前行的準備，讓每位法友都能法喜充滿\n\
                        此外，我們為了提升領隊跟導遊的素質，創辦了菩提邦朝聖學院，三年來，菩提邦印度團隊們開始\n\
                        每天供佛、繞塔、經行、禪修\n\
                        每天在大塔前排燈點燈祈福\n\
                        並且學習了華嚴經法華經楞嚴經\n\
                        以及佛陀的108則水平聖蹟\n\
                        他們，已經不只是導遊，更是聖地的守護者\n\
                        我們期盼，帶著大家一起回到印度\n\
                        一起更美好的自己相遇'
    ),
    ImagemapSendMessage(
        base_url='https://res.cloudinary.com/dljndh8rq/image/upload/v1687717149/india',
        alt_text='索取出團資訊',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            MessageImagemapAction(
                text='追尋釋尊足跡～經典印度朝聖13日',
                area=ImagemapArea(
                    x=26, y=167, width=472, height=343
                )
            ),
            MessageImagemapAction(
                text='經典印度朝聖15日',
                area=ImagemapArea(
                    x=546, y=172, width=469, height=334
                )
            ),
            MessageImagemapAction(
                text='印度佛陀八大聖地寺廟寺廟巡禮團19日',
                area=ImagemapArea(
                    x=23, y=553, width=479, height=340
                )
            ),
            MessageImagemapAction(
                text='獨立成團',
                area=ImagemapArea(
                    x=545, y=554, width=472, height=337
                )
            )
        ]
    )
    ]
    line_bot_api.reply_message(event.reply_token, message_list)