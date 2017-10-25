# -*- coding: utf-8 -*- 
import telebot
from telebot import types

TOKEN = '461778834:AAHQw5zLVx5PujytNHHP1KbLqbf6F5YNI2E' #Ponemos nuestro TOKEN generado con el @BotFather
mi_bot = telebot.TeleBot(TOKEN) #Creamos nuestra instancia "mi_bot" a partir de ese TOKEN



def listener(mensajes):  ##Cuando llega un mensaje se ejecuta esta función
    for m in mensajes:
        chat_id = m.chat.id
        if m.content_type == 'text':
            text = m.text


            #Se agregan eventos de teclado
            alegre="   "+b"\xE2\x9C\x85".decode("utf-8")+"  "
            naranja_alert="  "+b"\xF0\x9F\x94\xB6".decode("utf-8")+"  "+b"\xF0\x9F\x94\x98".decode("utf-8")+"  "
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
            mi_bot.send_message(chat_id, text, reply_markup=markup)

mi_bot.set_update_listener(listener) #registrar la funcion listener
mi_bot.polling()

