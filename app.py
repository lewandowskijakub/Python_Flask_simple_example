from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    user = {'name': 'CodeCool222'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['name'] + '''!</h1>
    </body>
</html>'''


if __name__ == '__main__':
    app.run()
