import telebot
import requests
import time
from background import keep_alive
API_KEY = "588822033:AAHLDF8M0a-4cQcUN_SQnsaIUFpZ0ROcWhs"
URL = "https://www.halooglasi.com/nekretnine/prodaja-kuca/beograd?cena_d_to=15555555&cena_d_unit=4&kvadratura_d_from=11&kvadratura_d_unit=1"

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["Start"])
def hello_func(message):
    bot.send_message(message.from_user.id, 'Hi, ver 6')
    req = requests.get(URL)
    print(req.status_code)

    for i in range(6*60*24*5):
        req = requests.get(URL)
        print(req.status_code)
        timeToSleep = 60
        bot.send_message(message.from_user.id, 'Request status: ' + str(req.status_code) + ' Time :' + str(timeToSleep) + 'sec' )

        time.sleep(timeToSleep)


@bot.message_handler()
def echo_func(message):
    bot.send_message(message.from_user.id, message.text)
    
keep_alive()
bot.polling()



