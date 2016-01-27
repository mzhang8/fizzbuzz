from flask import Flask
import twilio.twiml

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
	# Greet user
	resp = twilio.twiml.Response()
	resp.say("Hello noob, enter a number for Phone Buzz.")

	# Listen for caller to press key for number
	with resp.gather(finishOnKey=*, action="/handle-key", method="POST") as g:
		g.say("Enter a number and then press star to play Phone Buzz.")

	return str(resp)

@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
	# Handle number key presses from user
	digits_pressed = request.values.get('Digits', None)
	resp = twilio.twiml.Response()
	resp.say(str(digits_pressed))

	return str(resp)


if __name__ == '__main__':
    app.run(debug=True)


