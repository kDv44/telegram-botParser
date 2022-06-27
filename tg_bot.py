import time
import telebot
from main import news_list

API_KEY = '5586669103:AAH9qPNAy8kgkVEO0ELRgT2BmgbDAN8QByw'
channel_id = 't.me/motosport_newsUA_bot'
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(content_types=['text'])
def commands(message):
    if message.text == 'Start' or 'start':

        while True:
            post_text = news_list
            iter_ = news_list['news']

            if post_text['news'] != news_list['news']:
                bot.send_message(channel_id, news_list)
                time.sleep(1800)
    else:
        bot.send_message(message.from_user.id, 'Enter start')


bot.polling()
