from flask import (Flask,
                    render_template,
                    request, redirect)

app = Flask(__name__)  #path to folder

@app.route('/')
def index():
    return ('Hello World')
