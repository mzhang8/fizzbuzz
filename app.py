from flask import Flask
import twilio.twiml
app = Flask(__name__)


@app.route('/')
def hello():
    resp = twilio.twiml.Response()
	resp.say("Hello")

	return str(resp)

if __name__ == '__main__':
    app.run()


