runserver_text = '''from ${app_name} import app
app.run(debug=True)'''

init_text = '''from flask import Flask
app = Flask(__name__)

import ${app_name}.views'''

views_text = '''from flask import request, render_template
from ${app_name} import app

@app.route('/')
def index():
    return 'Hello World!'
    '''

jquery_tag = '''
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>'''

search_route = '''
@app.route('/search')
def search():
    #assumes you have a q parameter passed to you in the request
    query = request.args.get.('q','')
    #your magic here
    results = []
    return render_template('search.html', results=results)'''

search_html = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
    <title>Search ${app_name}</title>
</head>
<body>
    <h1>${app_name} Search Results</h1>
    <ul id="searchResults">
    {% for result in results %}
    	<li>{{ result }}</li>
    {% endfor %}
    </ul>
</body>
</html>'''

index_html ='''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
    <title>${app_name}</title>
</head>
<body>
    <h1>Welcom to ${app_name}!</h1>
</body>
</html>'''

