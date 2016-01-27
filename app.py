from flask import Flask
import twilio.twiml
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Twilio!"

if __name__ == '__main__':
    app.run()


