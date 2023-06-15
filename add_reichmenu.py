import requests
import json

headers = {"Authorization":"Bearer 3Ma92PMIfy790Z...","Content-Type":"application/json"}

body = {
    "alias": 'RICHMENU_ALIAS',
    "image": 'https://i.imgur.com/0KBhjYO.png',
    "metadata": {
        "chatBarText": '點此打開圖文選單',
        "selected": true,
        "size": { width: 2500, height: 1684 },
        "areas": [
        {
            "bounds": { x: 2325, y: 0, width: 175, height: 208 },
            "action": {
            "type": 'message',
            text: '/richmenuPlayground exit',
            },
        },
        {
            "bounds": { x: 2150, y: 0, width: 175, height: 208 },
            "action": {
            "type": 'uri',
            uri: 'https://developers.line.biz/en/docs/messaging-api/try-rich-menu/#try-richmenu-switch-action',
            },
        },
        {
            "bounds": { x: 0, y: 208, width: 300, height: 245 },
            "action": {
            "type": 'richmenuswitch',
            richMenuAliasId: 'playground-1',
            data: httpBuildQuery({ from: RICHMENU_ALIAS, to: 'playground-1' }),
            },
        },
        {
            "bounds": { x: 300, y: 208, width: 730, height: 245 },
            "action": {
            "type": 'richmenuswitch',
            richMenuAliasId: 'playground-4',
            data: httpBuildQuery({ from: RICHMENU_ALIAS, to: 'playground-4' }),
            },
        },
        {
            "bounds": { x: 0, y: 1100, width: 1250, height: 450 },
            "action": {
            "type": 'richmenuswitch',
            richMenuAliasId: 'playground-6',
            data: httpBuildQuery({ from: RICHMENU_ALIAS, to: 'playground-6' }),
            },
        },
        {
            "bounds": { x: 1250, y: 1100, width: 1250, height: 450 },
            "action": {
            "type": 'richmenuswitch',
            richMenuAliasId: 'playground-7',
            data: httpBuildQuery({ from: RICHMENU_ALIAS, to: 'playground-7' }),
            },
        },
        ],
    },
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)