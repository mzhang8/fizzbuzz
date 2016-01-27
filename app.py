from flask import Flask
import twilio.twiml

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
	# Greet user
	resp = twilio.twiml.Response()
	resp.say("Hello noob, enter a number and then press star to play Phone Buzz.")

	# Listen for caller to press keys for number

	g = resp.gather(action="/handle-key", method="POST", finishOnKey="*")

	resp.say("OK. Here we go.")

	#values = fizzbuzz(10)

	#for v in values:
	#	resp.pause(length=1)
	#	resp.say(v)

	return str(resp)

@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
	digits = request.values.get('Digits', None)
	values = fizzbuzz(digits)

	resp = twilio.twiml.Response()
	for v in values:
		resp.pause(length=1)
		resp.say(v)

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


