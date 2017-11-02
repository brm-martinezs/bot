from TwitterAPI import TwitterAPI
from datetime import datetime, date, time, timedelta
from pymongo import MongoClient

class Twitter:
    def traerTwitter(self, texto):
        api = TwitterAPI('DwDK8z8hhd1VBWToqKkEWraeN', 
        'QfFQ8HNGdFWZYphVu62Bsx6JtDA72FPA1onXZkYa5WQxJexi2V', 
        '782779396675477504-q8wnkKCQVcWVVJ2IqLxMxWGTi7aYWJD', 
        'WHYKEgHORfhEfHD4LgPM4LDgCbtEbUJTKwZCn8GQOQp1x')
        r = api.request('search/tweets', {'q':'Avianca AND ' + texto})
        contador = 1
        TP = Twitter()
        for item in r:
            existe = TP.getTweet(item['id_str'])
            if existe == 0:
                contador = TP.getLastIdTweet()
                contador = contador + 1
                TP.insertarTwitter(item['id_str'], item['text'], item['user']['id_str'], item['user']['screen_name'], item['user']['followers_count'], item['retweet_count'], item['favorite_count'], item['created_at'], contador)
    def insertarTwitter(self, codigo, texto, codUsuario, usuario, seguidores, rtweet, favoritos, fechaC, contador):
        connection="mongodb://brm2_us3r4pp:JLGhYDdMXIrI8y3n@127.0.0.1/callaut"
        mongo = MongoClient(connection)
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
        fechaCreacion = fechaC
        #enviado = 'N'
        ahora = datetime.now()
        fecha2 = "%Y-%m-%d %H:%M:%S"
        fecha = ahora.strftime(fecha2)
        mensaje5a = texto.find("RT")
        if mensaje5a == -1:
            enviado = 'N'
        else:
            enviado = 'S'
        tw = {"idText":idText,"texto":texto,"idUsuario":idUsuario,"arrobaUsuario":arrobaUsuario,"followers":followers,"retweet":retweet,"favorite":favorite,"cuentaInsert":cuentaInsert,"enviado":enviado,"fechaCreacion":fechaCreacion,"fecha":fecha}         
        collection.insert(tw)
        print("Se imprimio la info correctamente")
    def getTweet(self, codigo):
        connection="mongodb://brm2_us3r4pp:JLGhYDdMXIrI8y3n@127.0.0.1/callaut"
        mongo = MongoClient(connection)
        db = mongo.callaut
        collection = db.twitterBusqueda
        usuarios = collection.find({'idText': codigo }).count()
        return usuarios
    def getUltTweets(self):
        connection="mongodb://brm2_us3r4pp:JLGhYDdMXIrI8y3n@127.0.0.1/callaut"
        mongo = MongoClient(connection)
        db = mongo.callaut
        collection = db.twitterBusqueda
        usuarios = collection.find({'enviado': 'N'})
        return usuarios
    def actualizarTwitter(self, codigo, enviado):
        connection="mongodb://brm2_us3r4pp:JLGhYDdMXIrI8y3n@127.0.0.1/callaut"
        mongo = MongoClient(connection)
        db = mongo.callaut
        collection = db.twitterBusqueda
        idText = codigo
        enviado = enviado 
        ahora = datetime.now()
        fecha2 = "%Y-%m-%d %H:%M:%S"
        fechaEnvio = ahora.strftime(fecha2)
        collection.update({"idText":idText,"enviado":enviado},{"$set":{"enviado":"S","fechaEnvio":fechaEnvio}})
    def getLastIdTweet(self):
        connection="mongodb://brm2_us3r4pp:JLGhYDdMXIrI8y3n@127.0.0.1/callaut"
        mongo = MongoClient(connection)
        db = mongo.callaut
        collection = db.twitterBusqueda
        usuarios = collection.find().sort([('cuentaInsert',-1)]).limit(1)
        for usuario in usuarios:
            return usuario['cuentaInsert'] 