from flask import Flask
from flask import request
from flask import render_template
import time

app = Flask(__name__)

def long_load(query, dropdown, anumber, mail_to):
    time.sleep(10) #just simulating the waiting period
    return f"You typed: {query}, {dropdown}, {anumber}, mail_to"

@app.route('/')
def home():
    return render_template("index.html") 

@app.route('/', methods=['POST'])
def form(display=None):
    query = request.form['anything']
    dropdown = request.form['show_number']
    anumber = request.form['anumber']
    mail_to = request.form['mail_to']
    outcome = long_load(query, dropdown, anumber, mail_to)
    return render_template("done.html", display=outcome)

if __name__ == '__main__':
    #app.debug = True
    app.run()