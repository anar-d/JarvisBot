import telebot
from datetime import date, timedelta
from random import choice
from pyowm import OWM
from os import listdir

def Weather():
    tomorrow = str(date.today()+timedelta(days=1))
    tomorrow_ = str(date.today()+timedelta(days=2))
    tomorrow__ = str(date.today()+timedelta(days=3))

    owm = OWM(API_key, language='ru')

    fc = owm.three_hours_forecast('Moscow, RU')
    f = fc.get_forecast()
    wtr = {}

    weather1 = []
    weather2 = []
    weather3 = []

    for weather in f:
        wtr[weather.get_reference_time('iso')] = [str(weather.get_detailed_status()),
                                                  int(weather.get_temperature(unit='celsius')['temp'])]
    for time, status in wtr.items():
        if tomorrow in str(time):
            weather1.append(f'Завтра в {time[11:13]}:00 будет {status[0]} и {status[1]} градусов.')
        if tomorrow_ in str(time):
            weather2.append(f'Послезавтра в {time[11:13]}:00 будет {status[0]} и {status[1]} градусов.')
        if tomorrow__ in str(time):
            weather3.append(f'Послепослезавтра в {time[11:13]}:00 будет {status[0]} и {status[1]} градусов.')
    return weather1, weather2, weather3

bot = telebot.TeleBot(token)

wtr = Weather()

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(False, False)
    user_markup.row('/music')
    user_markup.row('/weather1', '/weather2', '/weather3')

    bot.send_message(message.from_user.id, 'Ну что, народ, погнали ...',
                     reply_markup=user_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == '/music':
        bot.send_message(message.from_user.id, 'Подожди пару минут')
        directory = "Музыка для Джарвиса"
        all_files_in_directory = listdir(directory)
        random_file = choice(all_files_in_directory)
        music = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, music)
        music.close()
    elif message.text == '/weather1':
        bot.send_message(message.from_user.id, '\n'.join(wtr[0]))
    elif message.text == '/weather2':
        bot.send_message(message.from_user.id, '\n'.join(wtr[0]))
        bot.send_message(message.from_user.id, '\n'.join(wtr[1]))
    elif message.text == '/weather3':
        bot.send_message(message.from_user.id, '\n'.join(wtr[0]))
        bot.send_message(message.from_user.id, '\n'.join(wtr[1]))
        bot.send_message(message.from_user.id, '\n'.join(wtr[2]))

bot.polling(none_stop=True, interval=0)
