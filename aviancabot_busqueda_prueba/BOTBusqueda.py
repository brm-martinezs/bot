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
        #user_report = m.from_user.username
        if m.content_type == 'text':
            text = m.text
            D = Twitter()
            D.traerTwitter(text) 
            existenTw = "0"
            resul = D.getUltTweets()
            for val in resul:
                existenTw = "1"
                cadena = "idTweet:"+val['idText']+" ~|~ @"+val['arrobaUsuario']+" | Followers: "+str(val['followers'])+" | Favs: "+str(val['favorite'])+" | Retweets: "+str(val['retweet'])+" | Fecha: "+str(val['fechaCreacionColombia'])+" | Tweet: "+val['texto']+" | Link: "+val['link']  
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

                    msjAlertId=call.message.message_id
                    msjAlertText=call.message.text
                    tweet=msjAlertText.split(' ~|~ ')
                    idTweeet=tweet[0]
                    idTweetsrt=str(idTweeet)
                    idTweetN=idTweetsrt.split(':')
                    textTweet=tweet[1]

                    user_nombre=call.from_user.first_name
                    user_apellido=call.from_user.last_name
                    user_report=user_nombre+" "+user_apellido
                    datosTweet=str(textTweet)
                    infoTweet=datosTweet.split(' | ')
                    infoTweetFol = infoTweet[1]
                    datosTweetFol=str(infoTweetFol)
                    infoFol=datosTweetFol.split(': ')
                    infoTweetFavs = infoTweet[2]
                    datosTweetFavs=str(infoTweetFavs)
                    infoFavs=datosTweetFavs.split(': ')
                    infoTweetRet = infoTweet[3]
                    datosTweetRet=str(infoTweetRet)
                    infoRet=datosTweetRet.split(': ')
                    infoTweetTex = infoTweet[5]
                    datosTweetTex=str(infoTweetTex)
                    infoTex=datosTweetTex.split('Tweet: ')
                    infoTweetFec = infoTweet[4]
                    datosTweetFec=str(infoTweetFec)
                    infoFec=datosTweetFec.split('Fecha: ')
                    infoTweetLink = infoTweet[6]
                    datosTweetLink=str(infoTweetLink)
                    infoLink=datosTweetLink.split('Link: ')
                    
                    ahora = datetime.now()
                    fecha2 = "%d-%m-%Y %H:%M:%S"
                    colombia = ahora.strftime(fecha2)

                    if call.data=='naranja':
                        
                        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'followers':infoFol[1],'favorite':infoFavs[1],'retweet':infoRet[1],'tweet':str(infoTex[1]),'usuario':str(infoTweet[0]),'fechaTweet':str(infoFec[1]),'link':str(infoLink[1]),'tipoAlerta':'naranja','UserReport':str(user_report),'fecha': datetime.now(),'fechaCol': colombia})
                        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)+" Usuario reporto: "+str(user_report)
                        mi_bot.send_message('-255372512',sendTexto)
                        mi_bot.send_message(chat_id,"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como naranja")
                    elif call.data=='amarilla':
                        
                        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'followers':infoFol[1],'favorite':infoFavs[1],'retweet':infoRet[1],'tweet':str(infoTex[1]),'usuario':str(infoTweet[0]),'fechaTweet':str(infoFec[1]),'link':str(infoLink[1]),'tipoAlerta':'amarilla','UserReport':str(user_report),'fecha': datetime.now(),'fechaCol': colombia})
                        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)+" Usuario reporto: "+str(user_report)
                        mi_bot.send_message('-255372512',sendTexto)
                        mi_bot.send_message(chat_id,"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como amarilla")
                    elif call.data=='azul':
                        
                        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'followers':infoFol[1],'favorite':infoFavs[1],'retweet':infoRet[1],'tweet':str(infoTex[1]),'usuario':str(infoTweet[0]),'fechaTweet':str(infoFec[1]),'link':str(infoLink[1]),'tipoAlerta':'azul','UserReport':str(user_report),'fecha': datetime.now(),'fechaCol': colombia})
                        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)+" Usuario reporto: "+str(user_report)
                        mi_bot.send_message('-255372512',sendTexto)
                        mi_bot.send_message(chat_id,"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como azul")
                    elif call.data=='verde':
                        
                        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'followers':infoFol[1],'favorite':infoFavs[1],'retweet':infoRet[1],'tweet':str(infoTex[1]),'usuario':str(infoTweet[0]),'fechaTweet':str(infoFec[1]),'link':str(infoLink[1]),'tipoAlerta':'verde','UserReport':str(user_report),'fecha': datetime.now(),'fechaCol': colombia})
                        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)+" Usuario reporto: "+str(user_report)
                        mi_bot.send_message('-255372512',sendTexto)
                        mi_bot.send_message(chat_id,"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como verde")
                    else:

                        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'followers':infoFol[1],'favorite':infoFavs[1],'retweet':infoRet[1],'tweet':str(infoTex[1]),'usuario':str(infoTweet[0]),'fechaTweet':str(infoFec[1]),'link':str(infoLink[1]),'tipoAlerta':'morada','UserReport':str(user_report),'fecha': datetime.now(),'fechaCol': colombia})
                        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)+" Usuario reporto: "+str(user_report)
                        mi_bot.send_message('-255372512',sendTexto)
                        mi_bot.send_message(chat_id,"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como morada")
            if existenTw == "0":
                mi_bot.send_message(chat_id,"No se han encontrado Tweets con la palabra "+ text)
                            
mi_bot.set_update_listener(listener) #registrar la funcion listener
mi_bot.polling(none_stop = True , timeout = 60)
raw_input()
