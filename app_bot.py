import telebot
from utils import ConvertException, СurrencyConverter
from config import TOKEN, keys

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
def help_help(message: telebot.types.Message):
    text = ('Чтобы начать работу введите команду боту: \n <имя валюты> \
    <в какую валюту>\
    <количество>\n \
    по команде /value можно получить список доступных валют')
    bot.reply_to(message, text)

@bot.message_handler(commands=['value'])
def value_key(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertException('Неправильно количество параметров')

        qoute, base, amount = values
        total_base = СurrencyConverter.currency_convert(qoute=qoute, base=base, amount=amount)

    except ConvertException as e:
        bot.reply_to(message, f'Не удалось обработать запрос по причине \n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать запрос по причине \n{e}')

    else:
        text = f'Стоимость {amount} {keys[qoute]} в {keys[base]}: {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)

