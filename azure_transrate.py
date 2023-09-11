# azure_translate.py
import requests , uuid
import os

def azure_translate(text, from_langage,to_language ,key,region):
    # サブスクリプションキーとエンドポイントを設定
    subscription_key = key
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # APIのURLを構築
    path = '/translate'
    constructed_url = endpoint + path

    # リクエストヘッダーを設定
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'Ocp-Apim-Subscription-Region': region,  # 例: 'westus2'
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # リクエストパラメータを設定
    params = {
        'api-version': '3.0',
        'to': to_language,
        'from': from_langage
    }

    # 送信するテキストをJSON形式で整形
    body = [{
        'text': text
    }]

    # APIリクエストを送信してレスポンスを取得
    response = requests.post(constructed_url, params=params, headers=headers, json=body)
    result = response.json()
    if 'error' in result:
        print(f"AZURE Transrate ERROR [{result['error']['code']}]:{result['error']['message']}")
        return

    # 翻訳されたテキストを返す
    return result[0]["translations"][0]["text"]

if __name__ == "__main__":
    azure_transrate_key = os.getenv("AZURE_Transrate_KEY")
    region = "japaneast"

    translated_text = azure_translate("Hello", 'en',"ja",azure_transrate_key,region)
    print("Translated text:", translated_text)