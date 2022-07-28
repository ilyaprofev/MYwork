# -*- coding: utf-8 -*-
import pyowm
import telebot
from telebot import types

#5a38931b02eff98c09a688a2f514d990
owm = pyowm.OWM('5a38931b02eff98c09a688a2f514d990', language ="ru")
bot = bot = telebot.TeleBot("5450407096:AAFph9drXdHUTz_WU9LrXOiZnnPO6i66ICM")




#@bot.message_handler(commands=['start'])
#def send_welcome(message):
#	bot.reply_to(message, "Все комады:\n/test - Узнать, какие контрольные планируются\n/deadline - Узнай дату сдачи важной работы\n/workload - Узнай загруженность на сегодня по предметам\n/event-Узнай какое мероприятие сегодня в школе \n/HW-Узнай домашнее задание на сегодня\nНапиши свой город и узнай прогноз погоды на сегодня:")
#clear_schedule
@bot.message_handler(commands=['start'])
def start(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2)
    btn_today = types.KeyboardButton('/Homework')
    btn_tomorrow = types.KeyboardButton('/Событие')
    btn_today1 = types.KeyboardButton('/Загруженности')
    btn_tomorrow1 = types.KeyboardButton('/Работы')
    btn = types.KeyboardButton('/Контрольные')
    btn_tomorrow2 = types.KeyboardButton('/Погода')
    keyboard_markup.add(btn_today, btn_tomorrow, btn_today1, btn_tomorrow1, btn, btn_tomorrow2)
    bot.send_message(message.chat.id, 'Тибе помочь?C:\Users\Admin\weatherp.py', reply_markup=keyboard_markup)

@bot.message_handler(commands=['Событие'])
def send_welcome(message):
	bot.reply_to(message, "День учителя ,надень белую рубашку , жилетку и брюки.")

@bot.message_handler(commands=['Homework'])
def send_welcome(message):
	bot.reply_to(message, " Русский язык - 368 и 371 и тест, параграф 10 \n Алгебра №475 \n География 48 Параграф \n ")

@bot.message_handler(commands=['Погода'])
def send_welcome(message):
	bot.reply_to(message, "Напиши город:")

@bot.message_handler(commands=['Загруженности'])
def send_welcome(message):
	bot.reply_to(message, "Уровень загруженности на сегодня 4/10 - терпимо.")

@bot.message_handler(commands=['Работы'])
def send_welcome(message):
	bot.reply_to(message, "Сдать доклад по истории, правление Петра 1.")

@bot.message_handler(commands=['Контрольные'])
def send_welcome(message):
	bot.reply_to(message, "Контрольная по русскому языку в среду.")

	


@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "В городе " + message.text + " " + w.get_detailed_status() + "\n"
	answer += "Температура сейчас  в районе " + str(temp) + " градусов""\n\n"

	if temp < 10:
		answer += "Сейчас очень холодно."
	elif temp <  20:
		answer += "Сейчас холодно, одевайся теплей!"	
	else:
		answer += "погода хорошая."

	bot.send_message(message.chat.id, answer)




bot.polling( none_stop = True )


bot.polling( none_stop = True )
