#twilio creds
REAL = {
	'SID':"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	'ATOKEN':"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	'PHONE':"+10000000000"
}

#email creds
EMAIL = {
    'email':'your email address',
    'pass':'password'
}

#for twilio voice
MESSAGE = {
	'say':"Hello, my name is . Please review my CV. Thank you. "
}

#for twilio SMS
messages = {'real': '''Hi {}, my name is .
Hope you are having a nice day. I have sent my CV through {} regarding
the position of {} at {}. Please review it and provide a response.
Note this message is automated and you will not be able to reach me
through this number. You may reach me through: 
\nEmail: youremailaddress \nphone:+10000000000\nThank you.'''}

#url to send sms api rquest
url = {'url':'url for twilio sms requests'}
