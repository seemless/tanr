import sys
import os

runserver_text = '''from {0} import app
app.run(debug=True)'''

init_text ='''from flask import Flask
app = Flask(__name__)

import {0}.views'''

views_text = '''from {0} import app

@app.route('/')
def index():
    return 'Hello World!'
    '''


def create_file(file_name, text, app_name):
    new_text = text.format(app_name)
    with open(file_name, 'w') as f:
        f.write(new_text)

def change_dir(cur):
    os.chdir(os.path.abspath(cur))
    print "changing directories!"
    print cur

def make_app(app_name):

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
    create_file('views.py', views_text, app_name)

def main(args):
    print os.getcwd()
    path = None
    app_name = args[0]

    if len(args) > 1:
        path = args[1]

    if path is not None and os.path.isdir(path):
        change_dir(path)
    
    make_app(app_name)

if __name__=='__main__':
    args = sys.argv[1:]
    main(args)

