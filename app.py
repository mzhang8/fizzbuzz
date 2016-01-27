from flask import Flask
from flask import request
import twilio.twiml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
	# Greet user
	resp = twilio.twiml.Response()
	resp.say("Hello.")

	# Listen for caller to press keys for number

	with resp.gather(action="/handle-key", method="POST", timeout="3") as g:
		g.say("Enter a number and then wait a few seconds to play Phone Buzz.")

	return str(resp)

@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
	digits = request.values.get('Digits', None)
	values = fizzbuzz(5)

	resp = twilio.twiml.Response()
	resp.say("OK... Here we go.")

	for v in values:
		resp.pause(length=1)
		resp.say(v)

	return str(resp)

def fizzbuzz(n):

	values = []
	for i in range(n):
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


