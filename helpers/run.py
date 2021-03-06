from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
import settings

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_people():
    """Respond to incoming requests."""
    resp = VoiceResponse()
    msg = settings.MESSAGE['say']
    resp.say(msg*3)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
