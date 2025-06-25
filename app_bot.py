import telebot

TOKEN = "7795631923:AAFSJSmbQes8jS40RFCI6YeML_7AkCqd9-w"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def function_name(message):
    bot.reply_to(message, "This is a message handler")

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass


# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass
