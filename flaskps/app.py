from os import path
from flask import Flask, render_template, g

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inicio.html')

if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run()