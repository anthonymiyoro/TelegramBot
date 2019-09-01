# import requests
# import re
# import telepot
# import urllib3

# from flask import Flask, request
# from teleflask import Teleflask
# from credentials import bot_token

# app = Flask(__name__)
# bot = Teleflask(bot_token, app)

# from teleflask.messages import TextMessage

# # You can leave this bit out if you're using a paid PythonAnywhere account
# proxy_url = "http://proxy.server:3128"
# telepot.api._pools = {
#     'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
# }
# telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# # end of the stuff that's only needed for free accounts

# secret = "A_SECRET_NUMBER"
# bot = telepot.Bot(bot_token)
# bot.setWebhook("https://AnthonyNderitu.pythonanywhere.com/{}".format(secret), max_connections=1)

# @app.route('/{}'.format(secret), methods=["POST"])
# def telegram_webhook():
#     update = request.get_json()
#     if "message" in update:
#         chat_id = update["message"]["chat"]["id"]
#         if "text" in update["message"]:
#             text = update["message"]["text"]
#             bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))
#         else:
#             bot.sendMessage(chat_id, "From the web: sorry, I didn't understand that kind of message")
#     return "OK"

# @app.route("/")
# def index():
#     return "This is a normal Flask page."
# # end def


# # Register the /start command
# @bot.command("start")
# def start(update, text):
#     # update is the update object. It is of type pytgbot.api_types.receivable.updates.Update
#     # text is the text after the command. Can be empty. Type is str.
#     return TextMessage("<b>Hello!</b> Thanks for using @" + bot.username + "!", parse_mode="html")
# # end def


# # register a function to be called for updates.
# @bot.on_update
# def foo(update):
#     from pytgbot.api_types.receivable.updates import Update
#     assert isinstance(update, Update)
#     # do stuff with the update
#     # you can use bot.bot to access the pytgbot.Bot's messages functions
#     if not update.message:
#         return
#         # you could use @bot.on_message instead of this if.
#     # end if
#     if update.message.new_chat_member:
#         return TextMessage("Welcome!")
#     # end if
# # end def

# if __name__ == "__main__":
#     app.run()



from flask import Flask, request
import telegram
from mastermind import get_response
from credentials import bot_token

global bot
global TOKEN
URL = "https://anthonynderitu.pythonanywhere.com/"
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
    return '.'


if __name__ == '__main__':
    app.run(threaded=True)