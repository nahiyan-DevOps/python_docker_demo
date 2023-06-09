from flask import Flask
app = Flask(__name__)
@app.route('/’)
def hello_world():
return 'Hello, Docker!'
@app.route('/bjit')
def bjit():
return 'Hello From, BJIT!'
@app.route('/about-me')
def about_me():
return 'Hi, This is Nahiyan'
