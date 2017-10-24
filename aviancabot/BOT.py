import sys
import telebot # Importamos las librería
import logging #Define funciones y clases para el manejo de errores
import string #Para acceder a las funciones de texto

from telebot import types
from telebot import util
from telebot import apihelper
from pymongo import MongoClient
from datetime import datetime
import time

#Se inicia la conexión a mongo
connection="mongodb://brm2_us3r4pp:JLGhYDdMXIrI8y3n@127.0.0.1/callaut"
mongo = MongoClient(connection)

#Se selecciona la base de datos
db=mongo.callaut

#Se selecciona la conexión
reportT = db.report_tweet


param_1= sys.argv[1]
#texto = '&lt;p color:&quot;style:red&quot;&gt;Rojo&lt;/p&gt; '+param_1
TOKEN = '415043230:AAElgeUG4kI1-bOmQEcF6UwyQxOvvxTwKM0'
tb = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
#Se agregan eventos de teclado
alegre="   "+b"\xE2\x9C\x85".decode("utf-8")+"  "
naranja_alert="  "+b"\xF0\x9F\x94\xB6".decode("utf-8")+"  "+b"\xF0\x9F\x94\x98".decode("utf-8")
amarilla_alert="   "+b"\xE2\x9A\xA0".decode("utf-8")+"  "
azul_alert="   "+b"\xF0\x9F\x94\xB7".decode("utf-8")+"  "
morada_alert="   "+b"\xF0\x9F\x94\xAF".decode("utf-8")+"  "

markup = types.InlineKeyboardMarkup(row_width=3)
naranja=types.InlineKeyboardButton(naranja_alert,callback_data='naranja')
amarilla=types.InlineKeyboardButton(amarilla_alert,callback_data='amarilla')
azul=types.InlineKeyboardButton(azul_alert,callback_data='azul')
verde=types.InlineKeyboardButton(alegre,callback_data='verde')
morada=types.InlineKeyboardButton(morada_alert,callback_data='morada')

markup.row(naranja,amarilla)
markup.row(azul,verde,morada)
#tb.send_message('-241066499', param_1,parse_mode='HTML') # Ejemplo tb.send_message('109556849', 'Hola mundo!')
tb.send_message('-229963093', param_1, reply_markup=markup) # Ejemplo tb.send_message('109556849', 'Hola mundo!')

