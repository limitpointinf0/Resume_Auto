import helpers.settings as settings
import helpers.attach as attach
from helpers.send_waves import *
import subprocess
import json
from twilio.rest import Client
import csv

#grabbing url
request = ['curl', 'http://localhost:4040/api/tunnels']
comm = subprocess.Popen(request, stdout=subprocess.PIPE)
response = comm.communicate()[0].decode('utf-8')
datajson = json.loads(response)
URL = datajson['tunnels'][0]['public_url']

#call, text, send email
client = Client(settings.REAL['SID'], settings.REAL['ATOKEN'])
with open('list.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for r in reader:
        print('sending email to:', r[1], r[2])
        attach.send_mail(settings.EMAIL['email'], settings.EMAIL['pass'], [r[1]], r[2] + ' position at ' + r[3], 'Please see resume.', use_tls=True)
        print('sending SMS to: ', r[4])
        txt = textMessage(settings.url['url'], settings.REAL['PHONE'], settings.messages['real'].format(r[0], r[5], r[2], r[3]), '{}:{}'.format(settings.REAL['SID'],settings.REAL['ATOKEN']), r[4])
        txt.send()
        print('calling: ', r[4])
        phone = phoneCall(r[4], r[0], settings.REAL['PHONE'], URL, client)
        phone.call()
        print('\n\n')
print('done.')
