import pyowm


owm = pyowm.OWM('54f5777e6808117d796cbfd98e963d6a', language = "ru")


place = input('Привет Мама!!! \n В каком городе/стране Ты хочешь узнать погоду?: ')


observation = owm.weather_at_place(place)

w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print('В городе ' + place + ' сейчас ' + w.get_detailed_status())

print('Температура воздуха в районе ' + str(temp))

if temp < 10:
    print('На улице жо...гхмм холодно, одевайся теплее! \n Люблю тебя, Твой Мума!!!')
elif temp < 20:
    print('На улице прохладно, возьми ветровку/кофту! \n Люблю тебя, Твой Мума!!!')
else:
    print('На улице тепло! Пей больше воды! \n Люблю тебя, Твой Мума!!!')