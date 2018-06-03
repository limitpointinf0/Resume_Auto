"""This is where you set your API credentials for Twilio"""
REAL = {
	'SID':"xxxxxxxxxxxxxxxxxxxxxxxxxxx",
	'ATOKEN':"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	'PHONE':"+10000000000"
}

"""This is the message you want the voice from Twilio to read to the person you call"""
MESSAGE = {
	'SAY':"Please review my CV. Thank you. "
}

"""This is the message you want to send by SMS"""
messages = {'real': 'abcdefghijklmnopqrstuvwxyz'}

creds = {'real': 'SID:ATOKEN'} #separated by colon

my_phone = {'phone':'+10000000000'} #your phone number

url = {'url':'https://...'} #the url to send your request to with curl for SMS
