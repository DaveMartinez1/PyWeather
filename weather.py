import requests
import colorama
import platform
import os

############----------############
#          By: LexaHck           #
#    https://github.com/LexaHck  #
#                                #
#     From the dark side...      #
#             -2023-             #
############----------############

# Variables globales
name_city = input("Ingresa el nombre de la ciudad: ")
name_country= input("Ingresa el nombre del pais: ")

#Funciones
def show_error(error):
    print(f"[!] Error: {error}!")

def clear():
    if platform.system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

def call_api(city,country):
    api_key = 'YOUR API KEY'
    api_url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}')

    w_data = api_url.json()
    if api_url.status_code == '404':
        show_error('Ciudad no encontrada')
    else:
        show_weather(w_data)

def show_weather(data):
    name = data['name']
    country = data['sys']['country']
    main = data['main']
    temp = main['temp']

    temp = float(temp) - 273.15

    clear()
    print("~ Datos meteorológicos ~\n")
    print(f"Pais: {country}")
    print(f"Ciudad: {name}")
    print(f"Temperatura: {round(temp, 1)} C°")

# Ejecucion
clear()
if name_city == '' or name_country == '':
    show_error('Debe rellenar toda la info')
else:
    call_api(name_city,name_country)
