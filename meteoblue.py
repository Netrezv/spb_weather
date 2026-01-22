import os
import telebot
import urllib
import datetime
from telebot import types

TELEBOT_TOKEN = os.getenv('TELEBOT_TOKEN')
METEOBLUE_OLD_TOKEN = os.getenv('METEOBLUE_OLD_TOKEN')
METEOBLUE_NEW_TOKEN = os.getenv('METEOBLUE_NEW_TOKEN')

bot = telebot.TeleBot(TELEBOT_TOKEN)

today = datetime.datetime.today() + datetime.timedelta(hours=3)
date_today = today.strftime("%#d.%m.%Y")
hour_now = today.strftime("%H")
tomorrow = datetime.datetime.today() + datetime.timedelta(hours=12)
date_tomorrow = tomorrow.strftime("%#d.%m.%Y")

#print('Today =',today)
#print('Tomorrow =',tomorrow)
#print('Hour now =',hour_now)
#print('Date Today =',date_today)
#print('Date Tomorrow =',date_tomorrow)

if int(hour_now) > 12:
#	url='http://my.meteoblue.com/visimage/meteogram_web?look=METER_PER_SECOND&apikey={METEOBLUE_NEW_TOKEN}&lat=59.9386&lon=30.3141&asl=11&tz=Europe%2FMoscow&lang=ru&city=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3'
	url=f"https://my.meteoblue.com/visimage/meteogram_web_hd?look=METER_PER_SECOND%2CCELSIUS%2CMILLIMETER&apikey={METEOBLUE_OLD_TOKEN}&temperature=C&windspeed=ms-1&precipitationamount=mm&winddirection=3char&city=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3&iso2=ru&lat=59.9386&lon=30.3141&asl=11&tz=Europe%2FMoscow&lang=ru&sig=1af5a8f7ef215125934757625e46107d"  
#	f = open('meteoblue.png','wb')
#	f.write(urllib.request.urlopen(url).read())
#	f.close()
	
	req = urllib.request.Request(
		url,
		headers={
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
		}
	)
	
	with urllib.request.urlopen(req) as response:
		data = response.read()
		
	with open("meteoblue.png", "wb") as f:
		f.write(data)
		
	bot.send_chat_action('@spb_weather', 'upload_photo')
	img = open('meteoblue.png', 'rb')
	bot.send_photo('@spb_weather', img, caption='#weather\nПрогноз погоды на утро ' + date_tomorrow)
	img.close()

else:
#	url='http://my.meteoblue.com/visimage/meteogram_web?look=METER_PER_SECOND&apikey={METEOBLUE_NEW_TOKEN}&lat=59.9386&lon=30.3141&asl=11&tz=Europe%2FMoscow&lang=ru&city=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3'
	url=f"https://my.meteoblue.com/visimage/meteogram_web_hd?look=METER_PER_SECOND%2CCELSIUS%2CMILLIMETER&apikey={METEOBLUE_OLD_TOKEN}&temperature=C&windspeed=ms-1&precipitationamount=mm&winddirection=3char&city=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3&iso2=ru&lat=59.9386&lon=30.3141&asl=11&tz=Europe%2FMoscow&lang=ru&sig=1af5a8f7ef215125934757625e46107d"
#	f = open('meteoblue.png','wb')
#	f.write(urllib.request.urlopen(url).read())
#	f.close()

	req = urllib.request.Request(
		url,
		headers={
    		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
		}
	)
	
	with urllib.request.urlopen(req) as response:
		data = response.read()
		
	with open("meteoblue.png", "wb") as f:
		f.write(data)
	
	bot.send_chat_action('@spb_weather', 'upload_photo')
	img = open('meteoblue.png', 'rb')
	bot.send_photo('@spb_weather', img, caption='#weather\nПрогноз погоды на день и вечер ' + date_today)
	img.close()
