runserver_text = '''from {0} import app
app.run(debug=True)'''

init_text ='''from flask import Flask
app = Flask(__name__)

import {0}.views'''

views_text = '''from flask import request, render_template
from {0} import app

@app.route('/')
def index():
    return 'Hello World!'
    '''

