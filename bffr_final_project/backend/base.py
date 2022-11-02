from flask import Flask

api = Flask(__name__)

@api.route('/')
def hello_world():
    # return render_template('index.html')
    return "hello world"