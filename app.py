from flask import Flask, current_app, request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/favicon.ico')
def get_fav():
    print(__name__)
    return current_app.send_static_file('img/favicon.ico')


@app.route('/easyocr', methods=["POST"])
def easyocr():
    request.form.get("")
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
