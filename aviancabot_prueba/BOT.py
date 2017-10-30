# -*- coding: utf-8 -*- 
import telebot
from telebot import types
from TwitterAPI import TwitterAPI

TOKEN = '461778834:AAHQw5zLVx5PujytNHHP1KbLqbf6F5YNI2E' #Ponemos nuestro TOKEN generado con el @BotFather
mi_bot = telebot.TeleBot(TOKEN) #Creamos nuestra instancia "mi_bot" a partir de ese TOKEN



class Twitter:
    def traerTwitter(self, texto):
        api = TwitterAPI('DwDK8z8hhd1VBWToqKkEWraeN', 
        'QfFQ8HNGdFWZYphVu62Bsx6JtDA72FPA1onXZkYa5WQxJexi2V', 
        '782779396675477504-q8wnkKCQVcWVVJ2IqLxMxWGTi7aYWJD', 
        'WHYKEgHORfhEfHD4LgPM4LDgCbtEbUJTKwZCn8GQOQp1x')
        r = api.request('search/tweets', {'q':'Avianca AND ' + texto})
        contador = 1
        for item in r:
            existe = D.getTweet(item['id_str'])
            if existe == 0:
                contador = D.getLastIdTweet()
                contador = contador + 1
                D.insertarTwitter(item['id_str'], item['text'], item['user']['id_str'], item['user']['screen_name'], item['user']['followers_count'], item['retweet_count'], item['favorite_count'], item['created_at'], contador)
    def insertarTwitter(self, codigo, texto, codUsuario, usuario, seguidores, rtweet, favoritos, fechaC, contador):
        mongo = MongoClient()
        db = mongo.callaut
        collection = db.twitterBusqueda
        idText = codigo
        texto = texto
        idUsuario = codUsuario
        arrobaUsuario = usuario
        followers = seguidores
        retweet = rtweet
        favorite = favoritos
        cuentaInsert = contador
        enviado = 'N' 
        fechaCreacion = fechaC
        ahora = datetime.now()
        fecha2 = "%Y-%m-%d %H:%M:%S"
        fecha = ahora.strftime(fecha2)
        tw = {"idText":idText,"texto":texto,"idUsuario":idUsuario,"arrobaUsuario":arrobaUsuario,"followers":followers,"retweet":retweet,"favorite":favorite,"cuentaInsert":cuentaInsert,"enviado":enviado,"fechaCreacion":fechaCreacion,"fecha":fecha}         
        collection.insert(tw)
        print("Se imprimio la info correctamente")
    def getTweet(self, codigo):
        mongo = MongoClient()
        db = mongo.callaut
        collection = db.twitterBusqueda
        usuarios = collection.find({'idText': codigo }).count()
        return usuarios
    def getLastIdTweet(self):
        mongo = MongoClient()
        db = mongo.callaut
        collection = db.twitterBusqueda
        usuarios = collection.find().sort([('cuentaInsert',-1)]).limit(1)
        for usuario in usuarios:
            return usuario['cuentaInsert'] 



def listener(mensajes):  ##Cuando llega un mensaje se ejecuta esta función
    for m in mensajes:
        chat_id = m.chat.id
        if m.content_type == 'text':
            text = m.text
            D = Twitter()
            D.traerTwitter(text) 

            #Se agregan eventos de teclado
            """
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
            mi_bot.send_message(chat_id, text, reply_markup=markup) """
            mi_bot.send_message(chat_id, text)

mi_bot.set_update_listener(listener) #registrar la funcion listener
mi_bot.polling()

