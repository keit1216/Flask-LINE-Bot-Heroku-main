import json

# 讀取 JSON 檔案
with open('/Users/blue/Downloads/Flask-LINE-Bot-Heroku-main/output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 現在 'data' 是一個字典，包含了 JSON 檔案的內容
print(data)