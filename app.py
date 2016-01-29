from flask import Flask
from flask import request

from twilio.util import RequestValidator
import twilio.twiml

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def play():
	# Validation
	auth_token = '0eaf817384a273b077e08dcfb187ef13' # input Auth Token here

	validator = RequestValidator(auth_token)
	url = 'https://phonebuzz-phase1.herokuapp.com/'


	params = {    # input parameter values here
		'CallSid': 'CA26227316e588e817ab2498d42b02e462',
		'Caller': '+19546517039',
		'From': '+19546517039',
		'To': '+17542129667'
	}

	twilio_signature = request.headers.get('X-Twilio-Signature')
	if validator.validate(url, params, twilio_signature): 
		r = twiml.Response()
		r.say("Twilio request verified.")

	# Greet user
	resp = twilio.twiml.Response()
	resp.say("Hello.")

	# Listen for caller to press keys for number
	with resp.gather(action="/handle-key", method="POST", timeout="5") as g:
		g.say("Enter a number and then wait a few seconds to play Phone Buzz.")

	return str(resp)


@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
	digits = request.values.get('Digits', None)
	values = fizzbuzz(int(digits))

	# Say fizz buzz sequence
	resp = twilio.twiml.Response()
	resp.say("OK... Here we go.")

	for v in values:
		resp.pause(length=1)
		resp.say(v)

	resp.pause(length=2)
	resp.say("Thank you for playing.")

	return str(resp)


def fizzbuzz(n):
	values = []

	# Store fizz buzz sequence up to n in order
	for i in range(1, n + 1):
		if i % 5 == 0 and i % 3 == 0:
			values.append("fizz buzz")
		elif i % 3 == 0:
			values.append("fizz")
		elif i % 5 == 0:
			values.append("buzz")
		else: 
			values.append(str(i))

	return values


if __name__ == '__main__':
    app.run(debug=True)


