from telegram.ext import Updater, CommandHandler
import requests
import re

# Ask for photo of dog from API
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    image_url = contents['url']
    return image_url

def bop(bot, update):
    # get url with dog photo
    url = get_url()
    # get id of person using the chatbot
    chat_id = update.message.chat_id
    # send photo to person using chatbot
    bot.send_photo(chat_id=chat_id, photo=url)
    
def main():
    updater = Updater('968529952:AAGAm0GUYnyxaUEBs2GKqrLG2wg11-gHp8M')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()
    
# If file is ran, run the main function
if __name__ == '__main__':
    print ("start")
    main()