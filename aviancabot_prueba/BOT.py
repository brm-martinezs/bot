import telebot

TOKEN = '461778834:AAHQw5zLVx5PujytNHHP1KbLqbf6F5YNI2E' #Ponemos nuestro TOKEN generado con el @BotFather
mi_bot = telebot.TeleBot(TOKEN) #Creamos nuestra instancia "mi_bot" a partir de ese TOKEN



def listener(mensajes):  ##Cuando llega un mensaje se ejecuta esta función
    for m in mensajes:
        chat_id = m.chat.id
        if m.content_type == 'text':
            text = m.text

            mi_bot.send_message(chat_id,"Me copio de tu \ntexto")
            mi_bot.send_message(chat_id, text)

mi_bot.set_update_listener(listener) #registrar la funcion listener
mi_bot.polling()

