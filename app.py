from flask import Flask, current_app
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/favicon.ico')
def get_fav():
    print(__name__)
    return current_app.send_static_file('img/favicon.ico')


if __name__ == '__main__':
    app.run()
