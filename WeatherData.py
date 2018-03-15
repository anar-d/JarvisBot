import datetime, pyowm, const

def Weather():
    tomorrow = str(datetime.date.today()+datetime.timedelta(days=1))
    tomorrow_ = str(datetime.date.today()+datetime.timedelta(days=2))
    tomorrow__ = str(datetime.date.today()+datetime.timedelta(days=3))

    owm = pyowm.OWM(const.API_key, language='ru')

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