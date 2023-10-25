from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import json

def analyze_passport(image_path):
    # 用你的 Azure Form Recognizer 資源的資訊替換以下值
    endpoint = "https://roc.cognitiveservices.azure.com/"  # 替換為您的 Azure Form Recognizer 服務終結點
    key = "21c7ce580aa24bbb87d8372d09b20494"  # 替換為您的 Azure Form Recognizer 服務金鑰

    # 創建 DocumentAnalysisClient
    client = DocumentAnalysisClient(endpoint, AzureKeyCredential(key))

    # 讀取護照影像
    with open(image_path, "rb") as image:
        image_bytes = image.read()

    # 發送影像到 Form Recognizer 服務
    poller = client.begin_analyze_document("prebuilt-layout", document=image_bytes)
    result = poller.result()

    # 解析結果並輸出為 JSON
    document_analysis = {
        "pages": []
    }
    for page in result.pages:
        page_info = {
            "number": page.page_number,
            "lines": []
        }
        for line in page.lines:
            page_info["lines"].append({
                "text": line.content,  # 將 'text' 改為 'content'
            })
        document_analysis["pages"].append(page_info)
    
    # 將結果輸出為 JSON
    with open("output.json", "w") as output_file:
        json.dump(document_analysis, output_file, indent=4)

# 調用函數，指定護照影像的路徑
analyze_passport("/Users/blue/Documents/簽證申辦資料/越南電子簽證/0930_kevin.jpg")
