from TwitterAPI import TwitterAPI
from datetime import datetime, date, time, timedelta
from pymongo import MongoClient
"""api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret) """
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
		fechaEnvio = ""
		tw = {"idText":idText,"texto":texto,"idUsuario":idUsuario,"arrobaUsuario":arrobaUsuario,"followers":followers,"retweet":retweet,"favorite":favorite,"cuentaInsert":cuentaInsert,"enviado":enviado,"fechaCreacion":fechaCreacion,"fecha":fecha,"fechaEnvio":fechaEnvio}         
		collection.insert(tw)
		print("Se imprimio la info correctamente")
	def getTweet(self, codigo):
		mongo = MongoClient()
		db = mongo.callaut
		collection = db.twitterBusqueda
		usuarios = collection.find({'idText': codigo }).count()
		return usuarios
	def getUltTweets(self):
		mongo = MongoClient()
		db = mongo.callaut
		collection = db.twitterBusqueda
		usuarios = collection.find({'enviado': 'N'})
		return usuarios
	def actualizarTwitter(self, codigo, enviado):
		mongo = MongoClient()
		db = mongo.callaut
		collection = db.twitterBusqueda
		idText = codigo
		enviado = enviado 
		ahora = datetime.now()
		fecha2 = "%Y-%m-%d %H:%M:%S"
		fechaEnvio = ahora.strftime(fecha2)
		collection.update({"idText":idText,"enviado":enviado},{"$set":{"enviado":"S","fechaEnvio":fechaEnvio}})
	def getLastIdTweet(self):
		mongo = MongoClient()
		db = mongo.callaut
		collection = db.twitterBusqueda
		usuarios = collection.find().sort([('cuentaInsert',-1)]).limit(1)
		for usuario in usuarios:
			return usuario['cuentaInsert']

D = Twitter()
"""
resul = D.getUltTweets()
for val in resul:
	print ( "idTweet:"+val['idText']+" ~|~ @"+val['arrobaUsuario']+" | Followers "+str(val['followers'])+" | Favs "+str(val['favorite'])+" | Retweets "+str(val['retweet'])+" | Tweet "+val['texto'] )	
	D.actualizarTwitter(val['idText'],val['enviado']) """
D.traerTwitter('pilotos')



