import sys
import os
import argparse

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

def build_views_file(args):
    
    if args.search:
        search_route = '''
@app.route('/search')
def search():
    #assumes you have a q parameter passed to you in the request
    query = request.args.get.('q','')
    #your magic here
    results = []
    return render_template('search.html', results=results)'''
        updated_views_text = views_text + search_route
        return updated_views_text

def create_file(file_name, text, app_name):
    new_text = text.format(app_name)
    with open(file_name, 'w') as f:
        f.write(new_text)

def change_dir(cur):
    os.chdir(os.path.abspath(cur))
    print "changing directories!"
    print cur

def make_app(args):
    app_name = args.app_name

    #create the top level directory
    os.mkdir(app_name)
    cur_dir = os.path.join(os.getcwd(), app_name)
    change_dir(cur_dir)

    #create the runserver.py file
    create_file('runserver.py',runserver_text, app_name)

    #create the app module
    os.mkdir(app_name)
    change_dir(os.path.join(os.getcwd(), app_name))

    #create __init__.py file
    create_file('__init__.py', init_text, app_name)

    #create views.py file
    views_text = build_views_file(args)
    create_file('views.py', views_text, app_name)

def main(args):
    print args
    print os.getcwd()

    if os.path.isdir(args.path):
        change_dir(args.path)
    
    make_app(args)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('app_name', help='The name of the new app')
    parser.add_argument('path', help='The path where you want the app to live.')
    parser.add_argument('-s', '--search', help="include a search endpoint",
                    action="store_true")
    args = parser.parse_args()
    main(args)

