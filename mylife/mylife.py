from flask import Flask, request, abort
from linebot import LineBotApi, WedhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMassage, TextSendMessage

app=Flask(__name__)

line_bot_api=LineBotApi('2009429061')
handler=WedhookHandler('2c4b958ca60c8bcba4e27a864e9cf333')

@handler.add(MessageEvent, message=TextMassage)
def handle_message(event):
    text=event.message.text #=届いた文字

    if text=="お小遣い":
        reply_message="金額"
    elif text=="生理":
        reply_message="記録したよ"
    elif text=="記念日":
        reply_message="詳細"
    else:
        reply_message=text
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_message)
    )

if __name__=="__main__":
    app.run