# -*- coding: utf-8 -*- 
import telebot
from telebot import types
from twitter import *

#Se inicia la conexión a mongo
#connection="mongodb://brm2_us3r4pp:JLGhYDdMXIrI8y3n@127.0.0.1/callaut"
mongo = MongoClient()
#Se selecciona la base de datos
db=mongo.callaut
#Se selecciona la conexión
reportT = db.report_tweet

TOKEN = '461778834:AAHQw5zLVx5PujytNHHP1KbLqbf6F5YNI2E' #Ponemos nuestro TOKEN generado con el @BotFather
mi_bot = telebot.TeleBot(TOKEN) #Creamos nuestra instancia "mi_bot" a partir de ese TOKEN

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
        mi_bot.send_message(chat_id,"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como naranja")
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
        mi_bot.send_message(chat_id,"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como amarilla")
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
        mi_bot.send_message(chat_id,"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como azul")
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
        mi_bot.send_message(chat_id,"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como verde")
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
        mi_bot.send_message(chat_id,"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como morada")
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
        mi_bot.send_message(chat_id,"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como naranja")

