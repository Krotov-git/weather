import pyowm


def predict_weather(t):
    if t < 10:
        print('На улице жо...гхмм холодно, одевайся теплее! \n Люблю тебя, Твой Мума!!!')
    elif t < 20:
        print('На улице прохладно, возьми ветровку/кофту! \n Люблю тебя, Твой Мума!!!')
    else:
        print('На улице тепло! Пей больше воды! \n Люблю тебя, Твой Мума!!!')


owm = pyowm.OWM('54f5777e6808117d796cbfd98e963d6a', language="ru")
cancel = True
print('Привет Мама!!! ')

# Но любая информация не есть True, не есть число 1
#while cancel == True:
#while cancel == 1:

# Любая информация воспринимается while и if как True
while cancel:
    place = input('В каком городе/стране Ты хочешь узнать погоду?: ')
    #TODO сделай проверку на наличие соединения с интернетом
    # в помощь конструкция try{} expect{}
    observation = owm.weather_at_place(place)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    # cbvc
    #TODO сделай проверку на непустой запрос
    # в форме "если запрос не пуст, то:
    if observation:
        print('В городе ' + place + ' сейчас ' + w.get_detailed_status())
        print('Температура воздуха в районе ' + str(temp))
        predict_weather(temp)
        repeat = input('Повтор? введите Y/N: ')
        if repeat == 'N' or repeat == 'n':
            cancel = 0
            print("Goodbay!")
    else:
        print('Нет данных')

# Любая информация воспринимается while и if как True
# Но любая информация не есть True, не есть число 1