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
    # owm_config['connection']['use_ssl'] = False
    # owm_config['connection']["verify_ssl_certs"] = False
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
