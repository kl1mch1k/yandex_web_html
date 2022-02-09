from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title> Mars </title>
                          </head>
                          <body>
                            <p>Человечество вырастает из детства.</p>
                            <p>Человечеству мала одна планета.</p>
                            <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
                            <p>И начнем с Марса!</p>
                            <p>Присоединяйся!</p>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
