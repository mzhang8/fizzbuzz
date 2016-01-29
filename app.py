from flask import Flask
from flask import request, redirect
import flask

from twilio.rest import TwilioRestClient
import twilio.twiml
 
# Input credentials
account_sid = "AC26ed550393d2ae7230ea12233b224a17"
auth_token = "0eaf817384a273b077e08dcfb187ef13"
client = TwilioRestClient(account_sid, auth_token)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	resp = twilio.twiml.Response()
		
	# Greet user
	resp.say("Hello.")

	# Listen for caller to press keys for number
	with resp.gather(action="/handle-key", method="POST", timeout="5") as g:
		g.say("Enter a number and then wait a few seconds to play Phone Buzz.")

	return flask.render_template('index.html')

@app.route("/call", methods=['POST'])
def call_twilio():
	phone_number = request.form['phone']

	# Check that input is a valid number and call
	if len(phone_number) == 10 and phone_number.isnumeric(): 
		phone_number = "+1" + phone_number
		call = client.calls.create(to=phone_number,  
                           from_="+17542129667", # Twilio number
                           url="https://phonebuzz-phase2.herokuapp.com/play")

	return redirect('/')

@app.route("/play", methods=['GET', 'POST'])	
def play():
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


