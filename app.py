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

    # if(msg == 'temp1'):
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         FlexSendMessage(
    #             alt_text = '測試',
    #             contents = json.load(open('temp1.json', 'r', encoding='utf-8'))
    #         )
    #     )
    # elif(msg == 'temp2'):
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         FlexSendMessage(
    #             alt_text = '測試',
    #             contents = json.load(open('temp2.json', 'r', encoding='utf-8'))
    #         )
    #     )

    # elif(msg == 'quick'):
    #     # quick reply
    #     line_bot_api.reply_message(event.reply_token,
    #     TextSendMessage(
    #     text="文字訊息",
    #     quick_reply=QuickReply(
    #         items=[
    #                 QuickReplyButton(
    #                     image_url="https://cdn-icons-png.flaticon.com/128/3917/3917261.png",
    #                     action=MessageAction(label="詢問出團日期",text="詢問出團日期")
    #                     ),
    #                 QuickReplyButton(
    #                     image_url="https://cdn-icons-png.flaticon.com/128/3917/3917261.png",
    #                     action=MessageAction(label="詢問出團日期",text="詢問出團日期")
    #                     ),
    #                 QuickReplyButton(
    #                     action=MessageAction(label="成團資訊",text="成團資訊")
    #                     )

    #                 ]
    #             )
    #         )
    #     )
    # elif(msg == 'map'):
    #     # imagemap
    #     # imagemap_message = ImagemapSendMessage(
    #     # base_url='https://github.com/keit1216/Flask-LINE-Bot-Heroku-main/tree/main/switzerland',
    #     # alt_text='this is an imagemap',
    #     # base_size=BaseSize(height=1830, width=1040),
    #     # actions=[
    #     #     URIImagemapAction(
    #     #         link_uri='https://switzerland-travel.tw/travel/eighteen/',
    #     #         area=ImagemapArea(
    #     #             x=19, y=601, width=492, height=366
    #     #         )
    #     #     ),
    #     #     URIImagemapAction(
    #     #         link_uri='https://switzerland-travel.tw/travel/【純瑞旅遊10日】收錄少女峰馬特宏峰白朗峰黃金/',
    #     #         area=ImagemapArea(
    #     #             x=529, y=600, width=492, height=369
    #     #         )
    #     #     ),
    #     #     URIImagemapAction(
    #     #         link_uri='https://switzerland-travel.tw/travel/germany-switzerland-10days/',
    #     #         area=ImagemapArea(
    #     #             x=19, y=995, width=494, height=369
    #     #         )
    #     #     ),
    #     #     URIImagemapAction(
    #     #         link_uri='https://switzerland-travel.tw/travel/10-days-in-switzerland/',
    #     #         area=ImagemapArea(
    #     #             x=527, y=997, width=496, height=364
    #     #         )
    #     #     ),
    #     #     URIImagemapAction(
    #     #         link_uri='https://switzerland-travel.tw/travel/br-milan-10days/',
    #     #         area=ImagemapArea(
    #     #             x=16, y=1394, width=497, height=361
    #     #         )
    #     #     ),
    #     #     URIImagemapAction(
    #     #         link_uri='https://switzerland-travel.tw/travel/10-days-in-switzerland-2/',
    #     #         area=ImagemapArea(
    #     #             x=529, y=1392, width=492, height=373
    #     #         )
    #     #     )
    #     # ]
    #     # )
    #     # line_bot_api.reply_message(event.reply_token, imagemap_message)

    #     # imagemap
    #     imagemap_message = ImagemapSendMessage(
    #     base_url='https://github.com/line/line-bot-sdk-nodejs/raw/master/examples/kitchensink/static/rich',
    #     alt_text='this is an imagemap',
    #     base_size=BaseSize(height=1040, width=1040),
    #     actions=[
    #         URIImagemapAction(
    #             link_uri='https://google.com/',
    #             area=ImagemapArea(
    #                 x=0, y=586, width=520, height=454
    #             )
    #         ),
    #         MessageImagemapAction(
    #             text='hello',
    #             area=ImagemapArea(
    #                 x=520, y=586, width=520, height=454
    #             )
    #         )
    #     ]
    #     )
    #     line_bot_api.reply_message(event.reply_token, imagemap_message)

    # elif ('出團資訊' in msg):
    #     imagemap_message = ImagemapSendMessage(
    #     base_url='https://res.cloudinary.com/dljndh8rq/image/upload/v1687509072/travelinfo',
    #     alt_text='索取出團資訊',
    #     base_size=BaseSize(height=1040, width=1040),
    #     actions=[
    #         MessageImagemapAction(
    #             text='索取13天行程資訊',
    #             area=ImagemapArea(
    #                 x=0, y=105, width=519, height=416
    #             )
    #         ),
    #         MessageImagemapAction(
    #             text='索取15天行程資訊',
    #             area=ImagemapArea(
    #                 x=520, y=106, width=520, height=414
    #             )
    #         ),
    #         MessageImagemapAction(
    #             text='索取18天行程資訊',
    #             area=ImagemapArea(
    #                 x=1, y=524, width=519, height=516
    #             )
    #         ),
    #         MessageImagemapAction(
    #             text='索取獨立成團資訊',
    #             area=ImagemapArea(
    #                 x=524, y=521, width=515, height=519
    #             )
    #         )
    #     ]
    #     )
    #     line_bot_api.reply_message(event.reply_token, imagemap_message)
    
    # elif ('按鈕3' in msg):
    #     imagemap_message = ImagemapSendMessage(
    #     base_url='https://res.cloudinary.com/dljndh8rq/image/upload/v1687509135/3btn',
    #     alt_text='按鈕3',
    #     base_size=BaseSize(height=1040, width=1040),
    #     actions=[
    #         MessageImagemapAction(
    #             text='索取行程資訊',
    #             area=ImagemapArea(
    #                 x=104, y=184, width=394, height=362
    #             )
    #         ),
    #         MessageImagemapAction(
    #             text='索取出團日期',
    #             area=ImagemapArea(
    #                 x=543, y=182, width=392, height=365
    #             )
    #         ),
    #         MessageImagemapAction(
    #             text='專人諮詢',
    #             area=ImagemapArea(
    #                 x=103, y=576, width=836, height=317
    #             )
    #         )
    #     ]
    #     )
    #     line_bot_api.reply_message(event.reply_token, imagemap_message)

    # elif(msg == '開始'):
    #     message_list = [
    #         TextSendMessage(text='你好 xxxx'),
    #         TextSendMessage(text='顯示圖片 我們擁有15年經驗'),
    #         ImagemapSendMessage(
    #             base_url='https://res.cloudinary.com/dljndh8rq/image/upload/v1687509072/travelinfo',
    #             alt_text='索取出團資訊',
    #             base_size=BaseSize(height=1040, width=1040),
    #             actions=[
    #                 MessageImagemapAction(
    #                     text='索取13天行程資訊',
    #                     area=ImagemapArea(
    #                         x=0, y=105, width=519, height=416
    #                     )
    #                 ),
    #                 MessageImagemapAction(
    #                     text='索取15天行程資訊',
    #                     area=ImagemapArea(
    #                         x=520, y=106, width=520, height=414
    #                     )
    #                 ),
    #                 MessageImagemapAction(
    #                     text='索取18天行程資訊',
    #                     area=ImagemapArea(
    #                         x=1, y=524, width=519, height=516
    #                     )
    #                 ),
    #                 MessageImagemapAction(
    #                     text='索取獨立成團資訊',
    #                     area=ImagemapArea(
    #                         x=524, y=521, width=515, height=519
    #                     )
    #                 )
    #             ]
    #         )
    #     ]
    #     line_bot_api.reply_message(event.reply_token, message_list)
    if "13日" in msg:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='追尋釋尊足跡~經典印度朝聖13日：\n⭐行程連結(:) https://lihi1.com/4LlNi \n\n感謝老法友的支持與愛護，\n目前各團均已有人接受報名\n報名狀況如下：\n\n❤️=已成團\n💚=準備成團\n\n\n10月3日：已報名7位\n❤️10月17日：已報名10位\n💚10月31日：已報名9位\n11月出發已額滿\n❤️12月5日：已報名12位\n❤️12月19日：已報名16位\n1月2日：已報名4位\n💚1月16日：已報名9位\n1月30日：已報名6位\n💚2月13日：已報名8位\n2月27日：已報名7位\n3月12日：已報名4位\n'))
    
    elif "15日" in msg:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='經典印度朝聖15日\n⭐行程連結(:) https://lihi3.cc/UGhJy\n請您參考\n💡正念在印度~印度佛陀聖地深度15日：\n9月17日：可報名17位\n10月1日：可報名19位\n10月15日：可報名20位\n❤️10月29日：可報名3位\n11月出發已額滿\n12月3日：可報名16位\n12月17日：可報名20位\n12月31日：可報名20位\n💚1月14日：可報名16位\n💚1月28日：可報名20位\n2月11日：可報名20位\n2月25日：可報名20位\n3月10日：可報名19位\n'))
        
    elif "19日" in msg:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='印度佛陀八大聖地寺廟巡禮團19日：\n⭐行程連結(:)https://lihi1.com/NIlvu\n\n感謝老法友的支持與愛護，\n目前各團均已有人接受報名\n報名狀況如下：\n\n❤️=已成團\n💚=準備成團\n\n❤️10月31日：已滿團\n11月出發已額滿\n💚12月5日：已報名9位\n1月2日：已報名5位\n1月23日：已報名5位\n2月13日：已報名6位\n3月5日：已報名2位'))

    elif "獨立成團" in msg:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='菩提邦有15年的印度朝聖經驗，如果您的人數超過15人，就可以考慮選擇獨立出團，菩提邦可以按照您的天數、預算為您量身訂做最適合您的朝聖行程，歡迎來電 02-77304119或是留言給我們 我們會盡快與您聯繫'))

    elif "關於點燈團隊" in msg:
        # message_image_1 = [
        #     TextSendMessage(text='菩提邦印度團隊從疫情開始，因為台灣法友的心願，團隊開始在菩提迦耶為大眾點燈，他們每天繞塔，每天供佛，每天點燈，只希望能夠將聖地的美好，傳達給每一位尊敬的法友，願我們能用這盞燈，祈求眾生能得遇佛法')
        #     ,ImageSendMessage(
        #     original_content_url = 'https://res.cloudinary.com/dljndh8rq/image/upload/v1687722478/map/v53kll5zrkqt6jmiuqda.jpg',
        #     preview_image_url = 'https://res.cloudinary.com/dljndh8rq/image/upload/v1687722478/map/v53kll5zrkqt6jmiuqda.jpg')
        # ]
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='菩提邦印度團隊從疫情開始，因為台灣法友的心願，團隊開始在菩提迦耶為大眾點燈，他們每天繞塔，每天供佛，每天點燈，只希望能夠將聖地的美好，傳達給每一位尊敬的法友，願我們能用這盞燈，祈求眾生能得遇佛法'))
    
    elif "去年點燈紀錄" in msg:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='菩提邦印度團隊每天都會將點燈的紀錄上傳到臉書上，歡迎大家一同分享 https://www.facebook.com/budhiparty'))
    
    elif "我要點燈" in msg:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='兔年點燈，菩提邦印度團隊會在2023年下半年每天在菩提迦耶為您點一盞燈，為您繞塔供佛祈福，想點燈者請填寫表單：\nhttps://forms.gle/3hRTEYK8mtq2jYvX9'))
    
    elif "朝聖地圖正面" in msg:
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(
            original_content_url = 'https://res.cloudinary.com/dljndh8rq/image/upload/v1687722478/map/v53kll5zrkqt6jmiuqda.jpg',
            preview_image_url = 'https://res.cloudinary.com/dljndh8rq/image/upload/v1687722478/map/v53kll5zrkqt6jmiuqda.jpg'))

    elif "朝聖地圖背面" in msg:
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(
            original_content_url = 'https://res.cloudinary.com/dljndh8rq/image/upload/v1687722478/map/rydk4fiiuohuiophe8a4.jpg',
            preview_image_url = 'https://res.cloudinary.com/dljndh8rq/image/upload/v1687722478/map/rydk4fiiuohuiophe8a4.jpg'))
        
    elif "紙本朝聖地圖" in msg:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='為了使更多法友了解印度，菩提邦製作了免費印度朝聖地圖提供大家索取，請填寫表單，我們會盡快為您處理\nhttps://forms.gle/JtLa9bSqTKFRpDwG6'))
    
    elif "講座內容" in msg:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='講座內容：\n● 為什麼要去印度朝聖？\n● 談談佛陀的八大聖地\n● 印度朝聖，注意事項大公開\n● 如何擁有殊勝難得的朝聖因緣\n'))

    elif "我要報名免費線上講座" in msg:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='▎線上印度朝聖講座來了  ▎\n\n追隨釋尊足跡，前往印度朝聖是許多佛教徒的心願，\n然而，去印度朝聖到底該如何籌備，聽到的卻總是隻字片語，\n為了使更多法友能夠更加充分地做好印度朝聖的前行準備\n使這一趟一生一次的心靈之旅能夠殊勝圓滿！\n菩提邦團隊在辦理免費線上講座，期許能讓更多人認識印度、瞭解朝聖，完成一生的心願。\n\n🙏報名連結：https://forms.gle/hKudeHHtDHHobt7J7\n\n講座內容：\n● 為什麼要去印度朝聖？\n● 談談佛陀的八大聖地\n● 印度朝聖，注意事項大公開\n● 如何擁有殊勝難得的朝聖因緣\n\n菩提邦團隊合十'))
        # get_message = event.message.text
        # # Send To Line
        # reply = TextSendMessage(text=f"{get_message}")
        # line_bot_api.reply_message(event.reply_token, reply)

@handler.add(PostbackEvent)
def handle_postback(event):
    postback_data = event.postback.data
    if ('出團資訊' in postback_data):
        imagemap_message = ImagemapSendMessage(
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
    line_bot_api.reply_message(event.reply_token, imagemap_message)

@handler.add(FollowEvent)
def handle_follow(event):
    message_list = [
    TextSendMessage(text='菩提邦創辦人有15年的印度朝聖經驗，\n服務超過2000海內外法友前往印度朝聖，\n菩提邦印度朝聖的宗旨是：\n「用心做好每一團 利益所有朝聖者」\n所以，\n我們一台車45人座只收20位，\n我們一團20位法友，\n由領隊導遊導遊助理三人服務，\n為了讓所有參團的法友能夠有收穫，\n我們每個月都會舉辦兩場說明會，\n一場是「如何擁有一次殊勝難得的朝聖因緣」，\n另一場則是「聖地與經典」，\n希望透過前行的準備，讓每位法友都能法喜充滿。\n此外，我們為了提升領隊跟導遊的素質，創辦了菩提邦朝聖學院，三年來，菩提邦印度團隊們開始每天供佛、繞塔、經行、禪修，\n每天在大塔前排燈點燈祈福，\n並且學習了華嚴經法華經楞嚴經，\n以及佛陀的108則水平聖蹟，\n他們已經不只是導遊，更是聖地的守護者，\n我們期盼帶著大家一起回到印度，\n一起更美好的自己相遇'),
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