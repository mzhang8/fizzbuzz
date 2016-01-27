"""from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()"""


from flask import Flask
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_fizzbuzz():
	"""Start the game of Phone Buzz!"""
	resp = twilio.twiml.Response()
	resp.say("Hello")
	
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)