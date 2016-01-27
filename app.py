from flask import Flask
import twilio.twiml

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
	# Greet user
	resp = twilio.twiml.Response()
	resp.say("Hello noob, enter a number for Phone Buzz.")

	# Listen for caller to press keys for number
	with resp.gather(finishOnKey=*) as g:
		g.say("Enter a number and then press star to play Phone Buzz.")

	# Retrieve number key presses 
	#digits_pressed = request.values.get('Digits', None)
	#resp.say(str(digits_pressed))

	return str(resp)


if __name__ == '__main__':
    app.run(debug=True)


