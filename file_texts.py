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

search_route = '''
@app.route('/search')
def search():
    #assumes you have a q parameter passed to you in the request
    query = request.args.get.('q','')
    #your magic here
    results = []
    return render_template('search.html', results=results)'''

