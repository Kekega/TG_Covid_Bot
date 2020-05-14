import covid19
import telebot

covid = covid19.COVID19()
bot = telebot.TeleBot('1100493131:AAHZryn4oJH-FpRXhthiApoaoXsJoI_qjng')


@bot.message_handler(comands=['start'])
def start(message):
	send_mess = f"<b>Hello, {message.from_user.first_name}!<\b>\nВведите страну"
	bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def mess(message):
	final_message = ""
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "сша":
		location = covid.getLocationByCountryCode("US")
	elif get_message_bot == "украина":
		location = covid.getLocationByCountryCode("UA")
	elif get_message_bot == "россия":
		location = covid.getLocationByCountryCode("RU")
	else:
		location = covid.getLatest()
		final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевшие: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"
	
	if final_message == "":
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"
	
	bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)
