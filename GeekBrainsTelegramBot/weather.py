# import packages inside python
import datetime

# import downloaded packages
import pytz
import pyowm.commons.exceptions
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from pyrogram import emoji

# import my local files
import config


def get_client():
    owm_config = get_default_config()
    owm_config['language'] = 'ru'
    return OWM(api_key=config.OWM_KEY, config=owm_config)


client = get_client()

weather_emojis = {
    'Rain': emoji.CLOUD_WITH_RAIN,
    'Snow': emoji.SNOWFLAKE,
    'Clear': emoji.SUN,
    'Clouds': emoji.CLOUD,
    'Drizzle': emoji.UMBRELLA_WITH_RAIN_DROPS,
    'Thunderstorm': emoji.CLOUD_WITH_LIGHTNING_AND_RAIN
}


def get_current_weather(city):
    mgr = client.weather_manager()
    try:
        w = mgr.weather_at_place(city)
    except pyowm.commons.exceptions.NotFoundError:
        return 'Не найден город'
    w = w.weather
    status = w.detailed_status
    w_emoji = weather_emojis.get(w.status)
    temp = w.temperature('celsius')['temp']
    temp_sign = '+' if temp > 0 else ''
    # Additional information
    wind = w.wind()['speed']
    humidity = w.humidity
    # Create message`s text
    msg = f'Погода в городе {city}: \n\n'
    msg += f'{status.title()} {w_emoji} \n'
    msg += f'Температура: {temp_sign}{int(temp)}°C {emoji.THERMOMETER} \n'
    msg += f'Ветер: {int(wind)} м/с {emoji.LEAF_FLUTTERING_IN_WIND} \n'
    msg += f'Влажность: {humidity}% {emoji.DROPLET}'
    return msg


def get_forecast(city):
    mgr = client.weather_manager()
    try:
        w = mgr.forecast_at_place(city, interval='3h')
    except pyowm.commons.exceptions.NotFoundError:
        return 'Не найден город'
    weather_list = w.forecast.weathers
    dates = []
    today = datetime.datetime.now(pytz.UTC).replace(hour=0, minute=0, second=0, microsecond=0)
    for day in range(1, 4):
        for hour in range(0, 24, 6):
            dates.append(today + datetime.timedelta(days=day, hours=hour))
    weather_list = list(filter(lambda x: x.reference_time('date') in dates, weather_list))
    hours = {
        0: f'{emoji.CRESCENT_MOON} Ночь',
        6: f'{emoji.SUNRISE} Утро',
        12: f'{emoji.SUN} День',
        18: f'{emoji.SUNSET} Вечер',
    }
    day_names = ['Завтра', 'Послезавтра', 'Через 3 дня']
    msg = f'{emoji.CALENDAR} Прогноз в городе {city} на 3 дня: \n\n'
    for day in range(3):
        msg += f'{day_names[day]} \n'
        for hour in range(4):
            weather = weather_list[day * 4 + hour]
            status = weather.detailed_status
            w_emoji = weather_emojis.get(weather.status)
            temp = weather.temperature('celsius')['temp']
            temp_sign = '+' if temp > 0 else ''
            hour = weather.reference_time('date').hour
            msg += f'{hours[hour]}: {temp_sign}{int(temp)}°C, {status} {w_emoji} \n'
        msg += '\n'
    return msg
