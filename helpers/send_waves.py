# Import the module
import codecs
import subprocess
import datetime
import traceback

class textMessage():

  def __init__(self, url, from_, message, creds, number):
    '''
    url(str): url to send request to
    from_(str): your phone number
    message(str): SMS body
    creds(str): credentials in the form XXXXXXX:XXXXXX
    '''
    self.tool = 'curl'
    self.url = url
    self.from_ = 'From=%s' % from_
    self.message = 'Body=%s' % message
    self.creds = creds
    self.number = 'To=%s' % number

  def send(self):
    
    request = [
          self.tool,
          self.url,
          '-X',
          'POST',
          '--data-urlencode',
          self.number,
          '--data-urlencode',
          self.from_,
          '--data-urlencode',
          self.message,
          '-u',
          self.creds
          ]
    message = subprocess.Popen(request, stdout=subprocess.PIPE)
    output = message.communicate()
    print(output)

class phoneCall():

  def __init__(self, number, name, from_, url, client_obj):
    '''
    number(str): phone no to receiver
    name(str): name of receiver
    from_(str): your phone number
    url(str): url of tunneled server
    account_sid(str), auth_token(str): credentials for Twilio API
    '''
    self.number = number
    self.name = name
    self.from_ = from_
    self.URL = url
    self.client = client_obj

  def call(self):
    '''makes the phone call'''
    try:
      call = self.client.calls.create(
        to=self.number,
        from_=self.from_,
        url=self.URL
        )
      print(call.sid, datetime.datetime.now())
    except:
      print(traceback.format_exc())
