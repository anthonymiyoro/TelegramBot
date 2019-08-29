# import requests
# import re

# from flask import Flask
# from telegram.ext import Updater, CommandHandler


# app = Flask(__name__)

# # Ask for photo of dog from API
# def get_url():
#     contents = requests.get('https://random.dog/woof.json').json()
#     image_url = contents['url']
#     return image_url

# def bop(bot, update):
#     # get url with dog photo
#     url = get_url()
#     # get id of person using the chatbot
#     chat_id = update.message.chat_id
#     # send photo to person using chatbot
#     bot.send_photo(chat_id=chat_id, photo=url)

# def main():
#     updater = Updater('968529952:AAGAm0GUYnyxaUEBs2GKqrLG2wg11-gHp8M')
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler('bop',bop))
#     updater.start_polling()
#     updater.idle()

# @app.route("/")
# def hello():
#     main()
#     return ("Hello World")


# if __name__ == "__main__":
#     app.run()


from flask import Flask, request
import telegram
from credentials import bot_token, bot_user_name,URL
from mastermind import get_response


global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    print("got text message :", text)

    response = get_response(text)
    bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

    return 'ok'

@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@app.route('/')
def index():
    return 'HomePage'


if __name__ == '__main__':
    app.run(threaded=True)