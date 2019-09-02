from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/hi')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "do_the_login()"
    else:
        return 'show_the_login_form()'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
