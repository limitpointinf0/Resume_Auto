from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
from settings import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = VoiceResponse()
    msg = MESSAGE['SAY']
    resp.say(msg*3)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
