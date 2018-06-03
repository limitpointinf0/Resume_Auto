import datetime
import traceback
from settings import *
from twilio.rest import Client
import time
import csv

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = REAL['SID']
auth_token = REAL['ATOKEN']
phone_no = REAL['PHONE']
client = Client(account_sid, auth_token)

def call_them(call_list, interval=300, times=5):
    '''takes a list of phone numbers and calls them.
       interval: length of time between each call
       times: amount of times you want to call'''
    for t in range(times):
        try:
            for i in call_list:
                call = client.calls.create(
                    to=i,
                    from_=phone_no,
                    url=URL
                )
                print(call.sid, datetime.datetime.now())
            time.sleep(interval)
        except:
            print(traceback.format_exc())


if __name__ == '__main__':
    with open('url.txt','r') as g:
        URL = g.read()
    INTERVAL = int(input('Interval (s): '))
    TIMES = int(input('Times (s):'))
    call_list = []
    with open('list.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            call_list.append(row[4])
    
    call_them(time.time(), call_list, interval=INTERVAL, times=TIMES)
