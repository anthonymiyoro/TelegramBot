from flask import Flask, request
import telegram
from bot_brains import get_response, bop
from credentials import bot_token
from nltk.chat.eliza import eliza_chatbot

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

    # # Run response function on the text we got as input
    # response = get_response(text)
    # print ("response", response)

    if text == "/start" or text == "/hello":
        bot.sendMessage(chat_id, "Hello, I'm the therapist.  How can I help?")
        print ("Init message")
    else:
        bot.sendMessage(chat_id, eliza_chatbot.respond(text))

    # bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

    # run function that provides replies to messeges
    # bop(bot, update, chat_id, msg_id)

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
    return "This is a Flask bot server :^)"


if __name__ == '__main__':

    app.run(threaded=True)