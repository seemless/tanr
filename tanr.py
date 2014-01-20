import sys
import os
import argparse
from string import Template
import file_texts

def build_views_file(args):
    views_text = file_texts.views_text
    if args.search:
        views_text += file_texts.search_route
    return views_text

def create_file(file_name, text, name):
    t = Template(text)
    new_text = t.substitute(app_name=name)
    with open(file_name, 'w') as f:
        f.write(new_text)

def change_dir(cur):
    os.chdir(os.path.abspath(cur))
    print "changing directories!"
    print cur

def make_templates(args):
    if args.search:
        create_file('search.html', file_texts.search_html, args.app_name)
    

def make_app(args):
    app_name = args.app_name

    #create the top level directory
    os.mkdir(app_name)
    cur_dir = os.path.join(os.getcwd(), app_name)
    change_dir(cur_dir)

    #create the runserver.py file
    create_file('runserver.py',file_texts.runserver_text, app_name)

    #create the app module
    os.mkdir(app_name)
    change_dir(os.path.join(os.getcwd(), app_name))

    #create __init__.py file
    create_file('__init__.py', file_texts.init_text, app_name)

    #create views.py file
    views_text = build_views_file(args)
    create_file('views.py', views_text, app_name)

    #create templates dir and files
    temp = 'templates'
    os.mkdir(temp)
    change_dir(os.path.join(os.getcwd(),temp))
    make_templates(args)

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

