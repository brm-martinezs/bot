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


#param_1= sys.argv[1]
#texto = '&lt;p color:&quot;style:red&quot;&gt;Rojo&lt;/p&gt; '+param_1
TOKEN = '415043230:AAElgeUG4kI1-bOmQEcF6UwyQxOvvxTwKM0'
tb = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
#Se agregan eventos de teclado
@tb.callback_query_handler(func=lambda call: call.data)  # Whenever the user taps the "more" button,
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
        tb.send_message('-228603616',sendTexto)
        tb.send_message('-229963093',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como naranja")
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
        tb.send_message('-199957072',sendTexto)
        tb.send_message('-229963093',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como amarilla")
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
        tb.send_message('-187033923',sendTexto)
        tb.send_message('-229963093',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como azul")
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
        tb.send_message('-245382751',sendTexto)
        tb.send_message('-229963093',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como verde")
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
        tb.send_message('-233757293',sendTexto)
        tb.send_message('-229963093',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como morada")
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
        tb.send_message('-228603616',sendTexto)
        tb.send_message('-229963093',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como naranja")
        
tb.polling()

raw_input()
