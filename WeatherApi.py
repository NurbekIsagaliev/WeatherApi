from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('f21be11cefb7feeeab4509aea53455a3',config_dict)
owm.supported_languages
mgr = owm.weather_manager()
place = input("V kakom gorode/strane?: ")
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]
print("В  " + place +"  сейчас  " + w.detailed_status)
print("Температура сейчас в районе "+str(temp))


