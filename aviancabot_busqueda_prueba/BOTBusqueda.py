# -*- coding: utf-8 -*- 
import telebot
from telebot import types
from twitter import *
from pymongo import MongoClient

#Se inicia la conexión a mongo
#connection="mongodb://brm2_us3r4pp:JLGhYDdMXIrI8y3n@127.0.0.1/callaut"
#mongo = MongoClient(connection)
mongo = MongoClient()
#Se selecciona la base de datos
db=mongo.callaut
#Se selecciona la conexión
reportT = db.report_tweet

TOKEN = '262726886:AAE6vRg0RV2XdJ335j7m41PIOH506gJWmaU' #Ponemos nuestro TOKEN generado con el @BotFather
#TOKEN = '461778834:AAHQw5zLVx5PujytNHHP1KbLqbf6F5YNI2E'
mi_bot = telebot.TeleBot(TOKEN) #Creamos nuestra instancia "mi_bot" a partir de ese TOKEN

def listener(mensajes):  ##Cuando llega un mensaje se ejecuta esta función
    for m in mensajes:
        chat_id = m.chat.id
        if m.content_type == 'text':
            text = m.text
            D = Twitter()
            D.traerTwitter(text) 
            existenTw = "0"
            resul = D.getUltTweets()
            for val in resul:
                existenTw = "1"
                cadena = "idTweet:"+val['idText']+" ~|~ @"+val['arrobaUsuario']+" | Followers "+str(val['followers'])+" | Favs "+str(val['favorite'])+" | Retweets "+str(val['retweet'])+" | Fecha "+str(val['fechaCreacionColombia'])+" | Tweet "+val['texto']+" | Link "+val['link']  
                D.actualizarTwitter(val['idText'],val['enviado'])
                #mi_bot.send_message(chat_id, cadena)
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
                mi_bot.send_message(chat_id, cadena, reply_markup=markup) 

                @mi_bot.callback_query_handler(func=lambda call: call.data)  # Whenever the user taps the "more" button,
                def alert_callback(call):
                    if call.data=='naranja':
                        msjAlertId=call.message.message_id
                        msjAlertText=call.message.text
                        tweet=msjAlertText.split(' ~|~ ')
                        idTweeet=tweet[0]
                        idTweetsrt=str(idTweeet)
                        idTweetN=idTweetsrt.split(':')
                        textTweet=tweet[1]
                        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'texto':textTweet,'tipoAlerta':'naranja','fecha': datetime.now()})
                        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)
                        mi_bot.send_message('-277422259',sendTexto)
                        mi_bot.send_message('-277422259',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como naranja")
                    elif call.data=='amarilla':
                        msjAlertId=call.message.message_id
                        msjAlertText=call.message.text
                        tweet=msjAlertText.split(' ~|~ ')
                        idTweeet=tweet[0]
                        idTweetsrt=str(idTweeet)
                        idTweetN=idTweetsrt.split(':')
                        textTweet=tweet[1]
                        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'texto':textTweet,'tipoAlerta':'amarilla','fecha': datetime.now()})
                        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)
                        mi_bot.send_message('-277422259',sendTexto)
                        mi_bot.send_message('-277422259',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como amarilla")
                    elif call.data=='azul':
                        msjAlertId=call.message.message_id
                        msjAlertText=call.message.text
                        tweet=msjAlertText.split(' ~|~ ')
                        idTweeet=tweet[0]
                        idTweetsrt=str(idTweeet)
                        idTweetN=idTweetsrt.split(':')
                        textTweet=tweet[1]
                        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'texto':textTweet,'tipoAlerta':'azul','fecha': datetime.now()})
                        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)
                        mi_bot.send_message('-277422259',sendTexto)
                        mi_bot.send_message('-277422259',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como azul")
                    elif call.data=='verde':
                        msjAlertId=call.message.message_id
                        msjAlertText=call.message.text
                        tweet=msjAlertText.split(' ~|~ ')
                        idTweeet=tweet[0]
                        idTweetsrt=str(idTweeet)
                        idTweetN=idTweetsrt.split(':')
                        textTweet=tweet[1]
                        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'texto':textTweet,'tipoAlerta':'verde','fecha': datetime.now()})
                        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)
                        mi_bot.send_message('-277422259',sendTexto)
                        mi_bot.send_message('-277422259',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como verde")
                    elif call.data=='morada':
                        msjAlertId=call.message.message_id
                        msjAlertText=call.message.text
                        tweet=msjAlertText.split(' ~|~ ')
                        idTweeet=tweet[0]
                        idTweetsrt=str(idTweeet)
                        idTweetN=idTweetsrt.split(':')
                        textTweet=tweet[1]
                        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'texto':textTweet,'tipoAlerta':'morada','fecha': datetime.now()})
                        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)
                        mi_bot.send_message('-277422259',sendTexto)
                        mi_bot.send_message('-277422259',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como morada")
                    else:
                        msjAlertId=call.message.message_id
                        msjAlertText=call.message.text
                        tweet=msjAlertText.split(' ~|~ ')
                        idTweeet=tweet[0]
                        idTweetsrt=str(idTweeet)
                        idTweetN=idTweetsrt.split(':')
                        textTweet=tweet[1]
                        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'texto':textTweet,'tipoAlerta':'naranja','fecha': datetime.now()})
                        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)
                        mi_bot.send_message('-277422259',sendTexto)
                        mi_bot.send_message('-277422259',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como naranja")
            if existenTw == "0":
                mi_bot.send_message(chat_id,"No se han encontrado Tweets con la palabra "+ text)
                            
mi_bot.set_update_listener(listener) #registrar la funcion listener
mi_bot.polling(none_stop = True , timeout = 60)