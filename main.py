import telebot

API_KEY = "588822033:AAHLDF8M0a-4cQcUN_SQnsaIUFpZ0ROcWhs"

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["Start"])
def hello_func(message):
    bot.send_message(message.from_user.id, 'Hi')

@bot.message_handler()
def echo_func(message):
    bot.send_message(message.from_user.id, message.text)

bot.polling()

