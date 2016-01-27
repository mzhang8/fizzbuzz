from flask import Flask
import twilio.twiml

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
	# Greet user
	resp = twilio.twiml.Response()
	resp.say("Hello noob, enter a number for Phone Buzz.")

	# Listen for caller to press keys for number
	#g = resp.gather(finishOnKey=*)
	#g.say("Enter a number and then press star to play Phone Buzz.")

	# Retrieve number key presses 
	#digits_pressed = request.values.get('Digits', None)
	#resp.say(str(digits_pressed))

	values = fizzbuzz(10)

	for v in values:
		twilio.twiml.Pause(2)
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


