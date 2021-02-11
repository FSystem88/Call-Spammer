#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot, requests, random, datetime, sys, time, argparse, json, re, sqlite3, os
from telebot import types
bot = telebot.TeleBot("")

try:
	owner = 355821673
	otchet = 843660312
	
	def MainMenu(message):
		keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.row('🚀 Быстрый спамер')
		keyboard.row('☎️ Номера', '👥 Группы')
		keyboard.row('🏠 Домой')
		bot.send_message(message.chat.id, '''Меню Спамера:''', reply_markup=keyboard)

	def AdminPanel(message):
		keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.row('Заблокировать пользователя')
		keyboard.row('Разблокировать пользователя')
		keyboard.row('Показать всех заблокированных')
		keyboard.row('Удалить номер из Антиспама')
		keyboard.row('Показать  все отчеты')
		keyboard.row('Отправить всем сообщение')
		keyboard.row('Новый прокси')
		keyboard.row('🏠 Домой')
		bot.send_message(message.chat.id, '''Админ панель:''', reply_markup=keyboard)


	@bot.message_handler(commands=['start'])
	def handle_start(message): 
		try:
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("SELECT * FROM BlackList WHERE id='{}'".format(message.chat.id))
			row = dbs.fetchall() 
			if row != []:
				bot.send_message(message.chat.id, "Вы добавлены в черный список.\nПо всем вопросам обращаться к @FSystem88")
			else:
				try:
					db = sqlite3.connect("users.db")
					dbs = db.cursor()
					dbs.execute("CREATE TABLE id"+f'{message.chat.id}'+" (`id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, phone text, count text)")
				except:
					pass
				keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
				if message.chat.id == owner:
					keyboard.row('⚡️ Спамер', '⚙ Настройки')
					keyboard.row('Админ панель')
				else:
					keyboard.row('⚡️ Спамер', '⚙ Настройки')
				bot.send_message(owner, '''Новый пользователь: <a href='tg://user?id={}'>{}</a>\nUsername: @{}\niD: {}'''.format(message.chat.id, message.chat.first_name, message.chat.username, message.chat.id), parse_mode="HTML")

				bot.send_message(message.chat.id, '''Привет, {}.\nЯ бот от @FSystem88.\nЭто простой смс спамер, который засрёт 1 или несколькоо номеров, которые тебе заблагорассудится.\n\nВообще как бы сервисов по отправки СМС много, но из-за того, что трафик проходит через VPN соединение (спасибо РКН за блокировку Telegram на территории РФ), то СМСки доходят не все.\nБуду решать эту проблему... возможно...'''.format(message.chat.first_name), reply_markup=keyboard)
		except:
			pass


	@bot.message_handler(commands=['restart'])
	def restart(message):
		try:
			bot.send_message(message.chat.id, "Спасибо. Я жив!")
			MainMenu(message)
		except:
			pass

	@bot.message_handler(func=lambda message: True, content_types=['text'])
	def Main(message):
		try:
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("SELECT * FROM BlackList WHERE id='{}'".format(message.chat.id))
			row = dbs.fetchall() 
			if row != []:
				bot.send_message(message.chat.id, "Вы добавлены в черный список.\nПо всем вопросам обращаться к @FSystem88")
			else:
				if message.text == '🏠 Домой':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					if message.chat.id == owner:
						keyboard.row('⚡️ Спамер', '⚙ Настройки')
						keyboard.row('Админ панель')
					else:
						keyboard.row('⚡️ Спамер', '⚙ Настройки')
					bot.send_message(message.chat.id, "Главное меню:",reply_markup=keyboard)
				elif message.text == '⚙ Настройки':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('🆘 Помощь')
					keyboard.row('📄 Антиспам')
					keyboard.row('💵 Донатерная')
					keyboard.row('📤 Отчёт')
					keyboard.row('🏠 Домой')
					bot.send_message(message.chat.id, "⚙ Настройки",reply_markup=keyboard)
				elif message.text == '🆘 Помощь':
					bot.send_message(message.chat.id, '''
Привет!
Это всего лишь говноспамер и ничего более ☺
Тут всё просто!

Мне было бы очень приятно, если бы ты подписался на мои каналы.
@spymer - канал спамера.
@FS88chan - личный канал.
@FS88chat - чат спамера и прочего оффтопа.
@FSystem88 - моя личка.
Спасибо!''')
				elif message.text == '💵 Донатерная':
					bot.send_message(message.chat.id, 'https://t.me/spymer/43')
				elif message.text == '📄 Антиспам':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('➕ Добавить номер')
					keyboard.row('🏠 Домой')
					bot.send_message(message.chat.id, '''Привет. Ты можешь добавить свой номер телефона в антиспам базу этого бота''', reply_markup=keyboard)
				elif message.text == '➕ Добавить номер':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('✖️ Отмена')
					bot.send_message(message.chat.id, '''Отправьте мне номер телефона в формате 7999xxxxxxx и я сохраню его в базу.''', reply_markup=keyboard)
					bot.register_next_step_handler(message, add_white)
				elif message.text == '➕ Добавить еще номер':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('✖️ Отмена')
					bot.send_message(message.chat.id, '''Отправьте мне номер телефона в формате 7999xxxxxxx и я сохраню его в базу.''', reply_markup=keyboard)
					bot.register_next_step_handler(message, add_white)
				elif message.text == 'Удалить номер из Антиспама':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('✖️ Отмена')
					bot.send_message(message.chat.id, '''Отправьте мне номер телефона в формате 7999xxxxxxx и я удалю его из базы.''', reply_markup=keyboard)
					bot.register_next_step_handler(message, del_white)	
				elif message.text == '⚡️ Спамер':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('🚀 Быстрый спамер')
					keyboard.row('☎️ Номера', '👥 Группы')
					keyboard.row('🏠 Домой')
					bot.send_message(message.chat.id, '''Меню Спамера:''', reply_markup=keyboard)
				elif message.text == '🚀 Быстрый спамер':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('✖️ Отмена')
					bot.send_message(message.chat.id, '''Введите номер телефона:''', reply_markup=keyboard)
					bot.register_next_step_handler(message, fastspam)
				elif message.text == '➕ Новый номер':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('✖️ Отмена')
					bot.send_message(message.chat.id, '''Введите новый номер телефона:''', reply_markup=keyboard)
					bot.register_next_step_handler(message, addphone)
				elif message.text == '👥 Группы':
					bot.send_message(message.chat.id, '''Ведётся разработка.''')
				elif message.text == '☎️ Номера':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('➕ Новый номер')
					keyboard.row('🏠 Домой')
					bot.send_message(message.chat.id, '''Ваши сохраненные номера:''', reply_markup=keyboard)
					db = sqlite3.connect("users.db")
					dbs = db.cursor()
					dbs.execute("SELECT * FROM id{}".format(message.chat.id))
					array = list(dbs.fetchall())
					for row in array:
						numb = row[0]
						phone = row[1]
						count = row[2]
						key = types.InlineKeyboardMarkup()
						but1 = types.InlineKeyboardButton(text="-1", callback_data="min_{}".format(numb))
						but2 = types.InlineKeyboardButton(text="▶️", callback_data="start_{}".format(numb))
						but3 = types.InlineKeyboardButton(text="+1", callback_data="pls_{}".format(numb))
						but4 = types.InlineKeyboardButton(text="Удалить", callback_data="del_{}".format(numb))					
						key.add(but1, but2, but3)
						key.add(but4)
						bot.send_message(message.chat.id, 'Телефон: +{}.\nКол-во потоков: {}'.format(phone, count), reply_markup=key)	
				elif message.text == '📤 Отчёт':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('➕ Добавить отчёт')
					keyboard.row('🏠 Домой')
					bot.send_message(message.chat.id, '''Ваши отчёты:''', reply_markup=keyboard)
					db = sqlite3.connect("users.db")
					dbs = db.cursor()
					dbs.execute("SELECT * FROM otchet WHERE user='{}'".format(message.chat.id))
					array = list(dbs.fetchall())
					for row in array:
						numb = row[0]
						tema = row[1]
						text = row[2]
						user = row[3]
						key = types.InlineKeyboardMarkup()
						but1 = types.InlineKeyboardButton(text="Удалить", callback_data="del_otchet_{}".format(numb))
						key.add(but1)
						bot.send_message(message.chat.id, '''
<b>Отчёт №{}</b>
<a href='tg://user?id={}'>Добавил</a>
<b>Тема:</b> <i>{}</i>
<b>Текст:</b>\n<i>{}</i>
						'''.format(numb, user, tema, text), reply_markup=key, parse_mode="HTML")
				elif message.text == '➕ Добавить отчёт':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('✖️ Отмена')
					bot.send_message(message.chat.id, '''Введите кратко тему отчёта:''', reply_markup=keyboard)
					bot.register_next_step_handler(message, addotchet1)
				elif message.text == 'Админ панель':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('Заблокировать пользователя')
					keyboard.row('Разблокировать пользователя')
					keyboard.row('Показать всех заблокированных')
					keyboard.row('Удалить номер из Антиспама')
					keyboard.row('Показать  все отчеты')
					keyboard.row('Отправить всем сообщение')
					keyboard.row('Новый прокси')
					keyboard.row('🏠 Домой')
					bot.send_message(message.chat.id, '''Админ панель:''', reply_markup=keyboard)
				elif message.text == 'Заблокировать пользователя':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('✖️ Отмена')
					bot.send_message(message.chat.id, '''Введите iD пользователя:''', reply_markup=keyboard)
					bot.register_next_step_handler(message, add_black)
				elif message.text == 'Разблокировать пользователя':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('✖️ Отмена')
					bot.send_message(message.chat.id, '''Введите iD пользователя:''', reply_markup=keyboard)
					bot.register_next_step_handler(message, del_black)
				elif message.text == 'Показать всех заблокированных':
					db = sqlite3.connect("users.db")
					dbs = db.cursor()
					dbs.execute("SELECT * FROM BlackList")
					array = list(dbs.fetchall())
					for row in array:
						numb = row[0]
						key = types.InlineKeyboardMarkup()
						but1 = types.InlineKeyboardButton(text="Удалить", callback_data="delblack_{}".format(numb))
						key.add(but1)
						bot.send_message(message.chat.id, '''
<a href='tg://user?id={}'>Пользователь {}</a>
						'''.format(numb, numb), reply_markup=key, parse_mode="HTML")
				elif message.text == 'Отправить всем сообщение':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('✖️ Отмена')
					bot.send_message(message.chat.id, '''Введите сообщение:''', reply_markup=keyboard)
					bot.register_next_step_handler(message, allsend)
				elif message.text == 'Показать  все отчеты':
					bot.send_message(message.chat.id, '''Все отчёты:''')
					db = sqlite3.connect("users.db")
					dbs = db.cursor()
					dbs.execute("SELECT * FROM otchet")
					array = list(dbs.fetchall())
					for row in array:
						numb = row[0]
						tema = row[1]
						text = row[2]
						user = row[3]
						key = types.InlineKeyboardMarkup()
						but1 = types.InlineKeyboardButton(text="Удалить", callback_data="del_otchet_{}".format(numb))
						key.add(but1)
						bot.send_message(message.chat.id, '''
<b>Отчёт №{}</b>
<a href='tg://user?id={}'>Добавил</a>
<b>Тема:</b> <i>{}</i>
<b>Текст:</b>\n<i>{}</i>
						'''.format(numb, user, tema, text), reply_markup=key, parse_mode="HTML")
				elif message.text == 'Новый прокси':
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('✖️ Отмена')
					bot.send_message(message.chat.id, '''Введите новый прокси:''', reply_markup=keyboard)
					bot.register_next_step_handler(message, proxy)




		except:
			pass


	@bot.callback_query_handler(func=lambda call: True)
	def inline(call):
		global phone
		global count
		if call.data[:3] == "min":
			numb=call.data[4:]
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("SELECT * FROM id{} WHERE id='{}'".format(call.message.chat.id, numb))
			array = list(dbs.fetchall())
			for row in array:
				numb= row[0]
				phone = row[1]
				count = row[2]
				count = int(count)
				if count-1 == 0:
					bot.answer_callback_query(call.id, show_alert=True, text="Ноль нельзя")
				else:
					count= count-1
					db = sqlite3.connect("users.db")
					dbs = db.cursor()
					dbs.execute("UPDATE id{} SET count='{}' WHERE id='{}'".format(call.message.chat.id, count, numb))
					db.commit()
					dbs.execute("SELECT * FROM id{} WHERE id='{}'".format(call.message.chat.id, numb))
					array = list(dbs.fetchall())
					for row in array:
						numb = row[0]
						phone = row[1]
						count = row[2]
						key = types.InlineKeyboardMarkup()
						but1 = types.InlineKeyboardButton(text="-1", callback_data="min_{}".format(numb))
						but2 = types.InlineKeyboardButton(text="▶️", callback_data="start_{}".format(numb))
						but3 = types.InlineKeyboardButton(text="+1", callback_data="pls_{}".format(numb))
						but4 = types.InlineKeyboardButton(text="Удалить", callback_data="del_{}".format(numb))					
						key.add(but1, but2, but3)
						key.add(but4)
						bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Телефон: +{}.\nКол-во потоков: {}'.format(phone, count), reply_markup=key)
		
		if call.data[:3] == "pls":
			numb=call.data[4:]
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("SELECT * FROM id{} WHERE id='{}'".format(call.message.chat.id, numb))
			array = list(dbs.fetchall())
			for row in array:
				numb= row[0]
				phone = row[1]
				count = row[2]
				count = int(count)
				if count+1 == 10000000:
					bot.answer_callback_query(call.id, show_alert=True, text="Больше 10000000 нельзя")
				else:
					count= count+1
					db = sqlite3.connect("users.db")
					dbs = db.cursor()
					dbs.execute("UPDATE id{} SET count='{}' WHERE id='{}'".format(call.message.chat.id, count, numb))
					db.commit()
					dbs.execute("SELECT * FROM id{} WHERE id='{}'".format(call.message.chat.id, numb))
					array = list(dbs.fetchall())
					for row in array:
						numb = row[0]
						phone = row[1]
						count = row[2]
						key = types.InlineKeyboardMarkup()
						but1 = types.InlineKeyboardButton(text="-1", callback_data="min_{}".format(numb))
						but2 = types.InlineKeyboardButton(text="▶️", callback_data="start_{}".format(numb))
						but3 = types.InlineKeyboardButton(text="+1", callback_data="pls_{}".format(numb))
						but4 = types.InlineKeyboardButton(text="Удалить", callback_data="del_{}".format(numb))					
						key.add(but1, but2, but3)
						key.add(but4)
						bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Телефон: +{}.\nКол-во потоков: {}'.format(phone, count), reply_markup=key)

		if call.data[:5] == "start":
			numb = call.data[6:]
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("SELECT * FROM id{} WHERE id='{}'".format(call.message.chat.id, numb))
			array = list(dbs.fetchall())
			for row in array:
				numb = row[0]
				phone = row[1]
				count = row[2]
				db = sqlite3.connect("users.db")
				dbs = db.cursor()
				dbs.execute("SELECT * FROM WhiteList WHERE phone='{}'".format(phone))
				row = dbs.fetchall() 
				if row != []:
					bot.send_message(call.message.chat.id, "Спам на этот номер телефона запрещен.\nПопробуйе другой номер.")
				else:
					keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
					keyboard.row('🔥 Запуск')
					bot.send_message(call.message.chat.id, '''Спам на этот номер телефона разрешен.\nТелефон: +{}\nКоличество потоков: {}'''.format(phone, count), reply_markup=keyboard)
					bot.register_next_step_handler(call.message, spammer)
		
		if call.data[:3] == "del":
			numb = call.data[4:]
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("DELETE FROM id{} WHERE id='{}'".format(call.message.chat.id, numb))
			db.commit()
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Номер телефона удалён")
		
		if call.data[:10] == "del_otchet":
			numb = call.data[11:]
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("DELETE FROM otchet WHERE id='{}'".format(numb))
			db.commit()
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отчёт удалён")

		if call.data[:8] == "delblack":
			numb = call.data[9:]
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("DELETE FROM BlackList WHERE id='{}'".format(numb))
			db.commit()
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пользователь разблокирован")


	def proxy(message):
		global proxy
		proxy = message.text
		if proxy == "✖️ Отмена":
			bot.send_message(message.chat.id, '''Обновление прокси отменено''')			
			keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
			keyboard.row('Заблокировать пользователя')
			keyboard.row('Разблокировать пользователя')
			keyboard.row('Показать всех заблокированных')
			keyboard.row('Удалить номер из Антиспама')
			keyboard.row('Показать  все отчеты')
			keyboard.row('Отправить всем сообщение')
			keyboard.row('Новый прокси')
			keyboard.row('🏠 Домой')
			bot.send_message(message.chat.id, '''Админ панель:''', reply_markup=keyboard)
		else:
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("UPDATE proxy SET proxy='{}'".format(proxy))
			db.commit()
			bot.send_message(message.chat.id, '''Обновление прокси выполнено''')			
			keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
			keyboard.row('Заблокировать пользователя')
			keyboard.row('Разблокировать пользователя')
			keyboard.row('Показать всех заблокированных')
			keyboard.row('Удалить номер из Антиспама')
			keyboard.row('Показать  все отчеты')
			keyboard.row('Отправить всем сообщение')
			keyboard.row('Новый прокси')
			keyboard.row('🏠 Домой')
			bot.send_message(message.chat.id, '''Админ панель:''', reply_markup=keyboard)
			
	def addotchet1(message):
		global tema
		global text
		tema = message.text
		if tema == "✖️ Отмена":
			keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
			keyboard.row('🆘 Помощь')
			keyboard.row('📄 Антиспам')
			keyboard.row('💵 Донатерная')
			keyboard.row('📤 Отчёт')
			keyboard.row('🏠 Домой')
			bot.send_message(message.chat.id, "Добавление отчета отменено",reply_markup=keyboard)
		else:
			bot.send_message(message.chat.id, "Введите полное описание проблемы:")
			bot.register_next_step_handler(message, addotchet2)

	def addotchet2(message):
		global tema
		global text
		text = message.text
		if text == "✖️ Отмена":
			keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
			keyboard.row('🆘 Помощь')
			keyboard.row('📄 Антиспам')
			keyboard.row('💵 Донатерная')
			keyboard.row('📤 Отчёт')
			keyboard.row('🏠 Домой')
			bot.send_message(message.chat.id, "Добавление отчета отменено",reply_markup=keyboard)
		else:
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("INSERT INTO otchet (tema, text, user, done) VALUES ('{}', '{}', '{}', 'no')".format(tema, text, message.chat.id))
			db.commit()
			bot.send_message(message.chat.id, "Добавлен новый отчет")
			bot.send_message(owner, "<a href='tg://user?id={}'>{}</a> добавил новый отчет".format(message.chat.id, message.chat.first_name), parse_mode="HTML")
			keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
			keyboard.row('➕ Добавить отчёт')
			keyboard.row('🏠 Домой')
			bot.send_message(message.chat.id, '''Ваши отчёты:''', reply_markup=keyboard)
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			if message.chat.id == owner:
				dbs.execute("SELECT * FROM otchet WHERE user={}".format(message.chat.id))
			dbs.execute("SELECT * FROM otchet WHERE user={}".format(message.chat.id))
			array = list(dbs.fetchall())
			for row in array:
				numb = row[0]
				tema = row[1]
				text = row[2]
				user = row[3]
				key = types.InlineKeyboardMarkup()
				but1 = types.InlineKeyboardButton(text="Удалить", callback_data="del_otchet_{}".format(numb))
				key.add(but1)
				bot.send_message(message.chat.id, '''
<b>Отчёт №{}</b>
<a href='tg://user?id={}'>Добавил</a>
<b>Тема:</b> <i>{}</i>
<b>Текст:</b>\n<i>{}</i>
				'''.format(numb, user, tema, text), reply_markup=key, parse_mode="HTML")
			

	


	def addphone(message):
		global phone
		phone = message.text
		try:
			if phone == '✖️ Отмена':
				keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
				keyboard.row('➕ Новый номер')
				keyboard.row('🏠 Домой')
				bot.send_message(message.chat.id, '''Добавление отменено''', reply_markup=keyboard)
			elif int(phone):
				bot.send_message(message.chat.id, '''Введите кол-во потоков для этого номера (max 10)''')
				bot.register_next_step_handler(message, addphone2)
		except:
			keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
			keyboard.row('➕ Новый номер')
			keyboard.row('🏠 Домой')
			bot.send_message(message.chat.id, '''Добавление отменено. Проверьте правильность введенных данных. Если всё нормально, то отправьте данное сообщение @FSystem88''', reply_markup=keyboard)
			
	def addphone2(message):		

		global phone
		global count
		count = message.text
		try:
			if count == '✖️ Отмена':
				keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
				keyboard.row('➕ Новый номер')
				keyboard.row('🏠 Домой')
				bot.send_message(message.chat.id, '''Добавление отменено''', reply_markup=keyboard)
			elif int(count):
				if int(count) > 10000000:
					count ="10"
					bot.send_message(message.chat.id, "Вы ввели количество потоков больше 10000000.\nПрисвоено максимальное значение.")
				phone = re.sub(r'[ ()--+]', '', phone)
				count = re.sub(r'[ ()--+]', '', count)
				if phone[0] == '8':
					phone = '7'+phone[1:]
				if phone[0] == '9':
					phone = '7'+phone
				db = sqlite3.connect("users.db")
				dbs = db.cursor()
				dbs.execute("INSERT INTO id{} (phone, count) VALUES ('{}', '{}')".format(message.chat.id, phone, count))
				db.commit()
				keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
				keyboard.row('➕ Новый номер')
				keyboard.row('🏠 Домой')
				bot.send_message(message.chat.id, "Добавлен новый номер телефона: {}.\nКол-во потоков: {}".format(phone, count), reply_markup=keyboard)
				db = sqlite3.connect("users.db")
				dbs = db.cursor()
				dbs.execute("SELECT * FROM id{}".format(message.chat.id))
				array = list(dbs.fetchall())
				for row in array:
					numb = row[0]
					phone = row[1]
					count = row[2]
					key = types.InlineKeyboardMarkup()
					but1 = types.InlineKeyboardButton(text="-1", callback_data="min_{}".format(numb))
					but2 = types.InlineKeyboardButton(text="▶️", callback_data="start_{}".format(numb))
					but3 = types.InlineKeyboardButton(text="+1", callback_data="pls_{}".format(numb))
					but4 = types.InlineKeyboardButton(text="Удалить", callback_data="del_{}".format(numb))					
					key.add(but1, but2, but3)
					key.add(but4)
					bot.send_message(message.chat.id, 'Телефон: +{}.\nКол-во потоков: {}'.format(phone, count), reply_markup=key)
		except:
			keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
			keyboard.row('➕ Новый номер')
			keyboard.row('🏠 Домой')
			bot.send_message(message.chat.id, '''Добавление отменено. Проверьте правильность введенных данных. Если всё нормально, то отправьте данное сообщение @FSystem88''', reply_markup=keyboard)

		

	def fastspam(message):
		global phone
		global count
		phone = message.text
		if phone == "✖️ Отмена":
			bot.send_message(message.chat.id, '''Быстрый запуск отменён''')
			MainMenu(message)
		else:
			try:
				if int(phone):
					phone = re.sub(r'[ ()--+]', '', phone)
					if phone[0] == '8':
						phone = '7'+phone[1:]
					if phone[0] == '9':
						phone = '7'+phone
					bot.send_message(message.chat.id, "Проверка на наличие в антиспам базе...")
					db = sqlite3.connect("users.db")
					dbs = db.cursor()
					dbs.execute("SELECT * FROM WhiteList WHERE phone='{}'".format(phone))
					row = dbs.fetchall() 
					if row != []:
						bot.send_message(message.chat.id, "Спам на этот номер телефона запрещен.\nПопробуйе другой номер.")
					else:
						bot.send_message(message.chat.id, "Введите количесво потоков (max 10):")
					bot.register_next_step_handler(message, fastspam2)
			except:
				bot.send_message(message.chat.id, "Ошибка. Проверьте правильность введенных данных.")
				MainMenu(message)
				

	def fastspam2(message):
		global phone
		global count
		count = message.text
		try:
			if count == "✖️ Отмена":
				bot.send_message(message.chat.id, '''Быстрый запуск отменён''')
				MainMenu(message)
			elif int(count) > 10: 
				bot.send_message(message.chat.id, '''Это больше 10 потоков. Сервер слабый. Присвоено максимальное значение:''')
				count = "10"
				keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
				keyboard.row('🔥 Запуск')
				bot.send_message(message.chat.id, '''
Спам на этот номер телефона разрешен.
Телефон: +{}
Количество потоков: {}'''.format(phone, count), reply_markup=keyboard)
				bot.register_next_step_handler(message, spammer)

		except:
			bot.send_message(message.chat.id, "Ошибка. Проверьте правильность введенных данных.")
			MainMenu(message)

	
	
	def allsend(message):
		global text
		text = message.text
		if text == "✖️ Отмена":
			bot.send_message(message.chat.id, '''Добавление в черный список отменено''')			
			AdminPanel(message)
		else:
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("SELECT name FROM sqlite_master WHERE type='table'")
			array = list(dbs.fetchall())
			for row in array:
				try:
					bot.send_message(row[0][2:], text)
				except:
					pass
			bot.send_message(message.chat.id, '''Отправлено.''', reply_markup=keyboard)
			AdminPanel(message)

	def add_white(message):
		global phone
		phone = message.text
		if phone == "✖️ Отмена": 
			keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
			keyboard.row('➕ Добавить еще номер')
			keyboard.row('🏠 Домой')
			bot.send_message(message.chat.id, "Добавление отменено", reply_markup=keyboard)
		else:
			phone = re.sub(r'[ ()--+]', '', phone)
			if phone[0] == '8':
				phone = '7'+phone[1:]
			if phone[0] == '9':
				phone = '7'+phone
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("INSERT INTO WhiteList (phone) VALUES ('{}')".format(phone))
			db.commit()
			keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
			keyboard.row('➕ Добавить еще номер')
			keyboard.row('🏠 Домой')
			bot.send_message(message.chat.id, "Добавлен номер телефона:\n{}.".format(phone), reply_markup=keyboard)
	
	def add_black(message):
		global phone
		numb = message.text
		if numb == "✖️ Отмена":
			bot.send_message(message.chat.id, '''Добавление в черный список отменено''')			
			AdminPanel(message)
		else:
			numb = re.sub(r'[ ()--+]', '', numb)
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("INSERT INTO BlackList (id) VALUES ('{}')".format(numb))
			db.commit()
			bot.send_message(message.chat.id, "<a href='tg://user?id={}'>Пользователь</a> заблокирован".format(numb), parse_mode="HTML")
			AdminPanel(message)

	def del_white(message):
		global phone
		phone = message.text
		if phone == "✖️ Отмена":
			bot.send_message(message.chat.id, '''Удаление отменено''')			
			AdminPanel(message)
		else:
			phone = re.sub(r'[ ()--+]', '', phone)
			if phone[0] == '8':
				phone = '7'+phone[1:]
			if phone[0] == '9':
				phone = '7'+phone
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("SELECT * FROM WhiteList WHERE phone='{}'".format(phone))
			row = dbs.fetchall() 
			if row == []:
				keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
				keyboard.row('Удалить еще номер')
				keyboard.row('🏠 Домой')
				bot.send_message(message.chat.id, "Номер {} не найден".format(phone), reply_markup=keyboard)
			else:
				dbs.execute("DELETE FROM WhiteList WHERE phone='{}'".format(phone))
				db.commit()
				keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
				keyboard.row('Удалить еще номер')
				keyboard.row('🏠 Домой')
				bot.send_message(message.chat.id, "Удален номер телефона:\n{}.".format(phone), reply_markup=keyboard)


	def del_black(message):
		global phone
		numb = message.text
		if numb == "✖️ Отмена":
			bot.send_message(message.chat.id, '''Удаление отменено''')			
			AdminPanel(message)
		else:
			db = sqlite3.connect("users.db")
			dbs = db.cursor()
			dbs.execute("SELECT * FROM BlackList WHERE id='{}'".format(numb))
			row = dbs.fetchall() 
			if row == []:
				bot.send_message(message.chat.id, "<a href='tg://user?id={}'>Пользователь</a> не найден".format(numb), reply_markup=keyboard)
				AdminPanel(message)
			else:
				dbs.execute("DELETE FROM BlackList WHERE id='{}'".format(numb))
				db.commit()
				bot.send_message(message.chat.id, "<a href='tg://user?id={}'>Пользователь</a> удалён из черного списка".format(numb), reply_markup=keyboard)
				AdminPanel(message)

	def spammer(message):
		global phone
		global count
		db = sqlite3.connect("users.db")
		dbs = db.cursor()
		dbs.execute("SELECT name FROM sqlite_master WHERE type='table'")
		array = list(dbs.fetchall())
		for row in array:
			proxy = row[0]
			proxies = {'http':'{}'.format(proxy), 'https':'{}'.format(proxy)}
		keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
		MainMenu(message)
		bot.send_message(owner, "Запущен спам на: {}.\nКол-во потоков: {}\nUser: <a href='tg://user?id={}'>{}</a>\nID: {}".format(phone, count, message.chat.id, message.chat.first_name, message.chat.id), parse_mode="HTML", reply_markup=keyboard)
		bot.send_message(message.chat.id, 'Запущен спам на: {}.\nКол-во потоков: {}'.format(phone, count), reply_markup=keyboard)
		iteration = 0
		count = int(count)
		_phone=phone
		if _phone[0] == '+':
			_phone = _phone[1:]
		if _phone[0] == '8':
			_phone = '7'+_phone[1:]
		if _phone[0] == '9':
			_phone = '7'+_phone
		_name = ''
		for x in range(12):
			_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
			password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
			username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		
		_email = _name+f'{iteration}'+'@gmail.com'
		email = _name+f'{iteration}'+'@gmail.com'

		requests.post("http://127.0.0.1:8080/attack/start", json={"number_of_cycles": count, "phone": _phone})

		#bot.send_message(message.chat.id, 'Закончен спам на: +{}.\nКол-во потоков: {}'.format(phone, count), reply_markup=keyboard)

except:
	pass

if __name__ == '__main__':
	while True:
		try:
			bot.polling(none_stop=True)
		except:
			time.sleep(1)
