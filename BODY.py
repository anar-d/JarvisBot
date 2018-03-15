import const, WeatherData, os, random, telebot

bot = telebot.TeleBot(const.token)

wtr = WeatherData.Weather()

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
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        music = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, music)
        music.close()
    elif message.text == '/weather1':
        for i in wtr[0]:
            bot.send_message(message.from_user.id, i)
    elif message.text == '/weather2':
        for i in wtr[0]:
            bot.send_message(message.from_user.id, i)
        for i in wtr[1]:
            bot.send_message(message.from_user.id, i)
    elif message.text == '/weather3':
        for i in wtr[0]:
            bot.send_message(message.from_user.id, i)
        for i in wtr[1]:
            bot.send_message(message.from_user.id, i)
        for i in wtr[2]:
            bot.send_message(message.from_user.id, i)

bot.polling(none_stop=True, interval=0)