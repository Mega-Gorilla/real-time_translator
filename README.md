# Rreal-Time Translator
このスクリプトは、仮想スピーカーの音声をリアルタイムで翻訳するソフトウェアです。

[Demo]
https://twitter.com/i/status/1701280046001037448

# インストール

このスクリプトを実行するには「VB-Audio (https://vb-audio.com/Cable/)」をインストールする必要があります。

```
git clone https://github.com/Mega-Gorilla/real-time_translator.git
cd  real-time_translator
pip install -r requirements.txt
```
# 設定

Windows 環境変数に、[AZURE_API_KEY],[AZURE_Transrate_KEY]を作成し、それぞれに[Azure Speech key],[Azure Transrate key]を入力し再起動する。

Main.pyを開き以下の部分を任意の設定に書き直す。

```
#settings
record_langage='en-US' # https://learn.microsoft.com/ja-jp/azure/ai-services/speech-service/language-support?tabs=stt
from_langage='en' # https://learn.microsoft.com/ja-jp/azure/ai-services/translator/language-support
to_langage='ja' # https://learn.microsoft.com/ja-jp/azure/ai-services/translator/language-support
Stream_Speaker_Name = 'LG Ultra HD'
```

- record_langage → 再生する音源の言語(Speech to Text)
- from_langage → 再生する音源の言語(Transrate)
- to_langage → 翻訳先言語(Transrate)
- Stream_Speaker_Name → VB-Audio Speakerを用いるため、音声が聞こえなくなるため、音声をストリームするスピーカーを入力(デフォルトのスピーカー名を選択する。)

# 使い方
1. Windowsの再生スピーカーを、VB-Audio スピーカーに設定。
1. main.pyを実行