import pyowm
import telebot
#5a38931b02eff98c09a688a2f514d990
owm = pyowm.OWM('5a38931b02eff98c09a688a2f514d990', language ="ru")
bot = bot = telebot.TeleBot("5450407096:AAFph9drXdHUTz_WU9LrXOiZnnPO6i66ICM")







@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Все комады:\n/event-Узнай какое мероприятие сегодня в школе \n/HW-Узнай что сегодня задали нa дом \n Напиши свой город и узнай прогноз погоды на сегодня:")




@bot.message_handler(commands=[ 'event'])
def send_welcome(message):
	bot.reply_to(message, "День учителя ,одень белую рубашку , жилетку и брюки")



@bot.message_handler(commands=['HW'])
def send_welcome(message):
	bot.reply_to(message, " Русский - 368 и 371 и тест Парагроф 10 \n Алгебра 475н \n География 48Порогроф \n ")



@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += "Температура сейчас  в районе " + str(temp) + "градусов""\n\n"

	if temp < 10:
		answer += "Сейчас очень холодно."
	elif temp <  20:
		answer += "Сейчас холодно, одевайся теплей!"
	else:
		answer += "погода хорошая."

	bot.send_message(message.chat.id, answer)




bot.polling( none_stop = True )