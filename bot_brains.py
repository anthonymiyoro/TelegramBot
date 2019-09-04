import requests
from credentials import bot_token
from nltk.chat.eliza import eliza_chatbot

# Load JSON data
def get_response(text, bot, chat_id):
    """
    You can place your mastermind AI here
    could be a very basic simple response like "معلش"
    or a complex LSTM network that generate appropriate answer
    """
    if text == "/start" or text == "/hello":
        bot.sendMessage(chat_id, "Hello, I'm the therapist.  How can I help?")
    else:
        bot.sendMessage(chat_id, eliza_chatbot.respond(text))

    return "I can answer!"

def bop(bot, update, chat_id, msg_id):
    # get url with dog photo
    url = get_url()
    # get id of person using the chatbot
    chat_id = update.message.chat_id
    # send photo to person using chatbot
    bot.send_photo(chat_id=chat_id, photo=url)