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
        tb.send_message('-228603616',sendTexto)
        tb.send_message('-229963093',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como naranja")
    elif call.data=='amarilla':

        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'followers':infoFol[1],'favorite':infoFavs[1],'retweet':infoRet[1],'tweet':str(infoTex[1]),'usuario':str(infoTweet[0]),'fechaTweet':str(infoFec[1]),'link':str(infoLink[1]),'tipoAlerta':'amarilla','UserReport':str(user_report),'fecha': datetime.now(),'fechaCol': colombia})
        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)+" Usuario reporto: "+str(user_report)
        tb.send_message('-199957072',sendTexto)
        tb.send_message('-229963093',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como amarilla")
    elif call.data=='azul':

        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'followers':infoFol[1],'favorite':infoFavs[1],'retweet':infoRet[1],'tweet':str(infoTex[1]),'usuario':str(infoTweet[0]),'fechaTweet':str(infoFec[1]),'link':str(infoLink[1]),'tipoAlerta':'azul','UserReport':str(user_report),'fecha': datetime.now(),'fechaCol': colombia})
        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)+" Usuario reporto: "+str(user_report)
        tb.send_message('-187033923',sendTexto)
        tb.send_message('-229963093',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como azul")
    elif call.data=='verde':

        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'followers':infoFol[1],'favorite':infoFavs[1],'retweet':infoRet[1],'tweet':str(infoTex[1]),'usuario':str(infoTweet[0]),'fechaTweet':str(infoFec[1]),'link':str(infoLink[1]),'tipoAlerta':'verde','UserReport':str(user_report),'fecha': datetime.now(),'fechaCol': colombia})
        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)+" Usuario reporto: "+str(user_report)
        tb.send_message('-245382751',sendTexto)
        tb.send_message('-229963093',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como verde")
    else:

        reportT.insert_one({'idMensaje':msjAlertId,'idTweeet':idTweetN[1],'followers':infoFol[1],'favorite':infoFavs[1],'retweet':infoRet[1],'tweet':str(infoTex[1]),'usuario':str(infoTweet[0]),'fechaTweet':str(infoFec[1]),'link':str(infoLink[1]),'tipoAlerta':'morada','UserReport':str(user_report),'fecha': datetime.now(),'fechaCol': colombia})
        sendTexto="Mensaje ID "+str(msjAlertId)+" Texto: "+str(textTweet)+" "+str(idTweeet)+" Usuario reporto: "+str(user_report)
        tb.send_message('-228603616',sendTexto)
        tb.send_message('-229963093',"el Tweet("+textTweet[:80]+"...)Se reportó el tweet como naranja")
        
tb.polling()

raw_input()
