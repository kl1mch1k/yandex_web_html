from flask import Flask, url_for, request

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


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title> Привет, Марс! </title>
                          </head>
                          <body>
                            <h1> Жди нас, Марс! </h1>
                            <img src="{url_for('static', filename='img/mars.jpg')}"
                            alt="здесь должна была быть картинка, но не нашлась">
                            <p>Вот она какая, красная планета.</p>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet" type="text/css" href="
                                {url_for('static', filename='css/style.css')}" />
                                <link rel="stylesheet" 
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                crossorigin="anonymous">
                                <title> Привет, Марс! </title>
                              </head>
                              <body>
                                <h1> Жди нас, Марс! </h1>
                                <img src="{url_for('static', filename='img/mars.jpg')}"
                                alt="здесь должна была быть картинка, но не нашлась">
                                <div class="alert alert-dark" role="alert">
                                Человечество вырастает из детства.
                                </div>
                                <div class="alert alert-success" role="alert">
                                Человечеству мала одна планета.
                                </div>
                                <div class="alert alert-secondary" role="alert">
                                Мы сделаем обитаемыми безжизненные пока планеты.
                                </div>
                                <div class="alert alert-warning" role="alert">
                                И начнем с Марса!
                                </div>
                                <div class="alert alert-danger" role="alert">
                                Присоединяйся!
                                </div>'''


@app.route('/choice/<planet_name>')
def planet_name(planet_name):
    return f'''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet" 
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                    crossorigin="anonymous">
                                    <title> Варианты выбора </title>
                                  </head>
                                  <body>
                                    <h1> Мое предложение: {planet_name} </h1>
                                    <div class="alert alert-dark" role="alert">
                                    <h2> a </h2>
                                    </div>
                                    <div class="alert alert-success" role="alert">
                                    <h2> a </h2>
                                    </div>
                                    <div class="alert alert-secondary" role="alert">
                                    <h2> a </h2>
                                    </div>
                                    <div class="alert alert-warning" role="alert">
                                    <h2> a </h2>
                                    </div>
                                    <div class="alert alert-danger" role="alert">
                                    <h2> a </h2>
                                    </div>'''

@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                                    <html lang="en">
                                      <head>
                                        <meta charset="utf-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                        <link rel="stylesheet" 
                                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                        crossorigin="anonymous">
                                        <title> Результаты </title>
                                      </head>
                                      <body>
                                        <h1> Результаты отбора </h1>
                                        <div class="alert alert-dark" role="alert">
                                        <h2> Претендента на участие в миссии {nickname} </h2>
                                        </div>
                                        <div class="alert alert-success" role="alert">
                                        <h2> Уровень: {level} </h2>
                                        </div>
                                        <div class="alert alert-secondary" role="alert">
                                        <h2> Рейтинг: {rating} </h2>
                                        </div>
                                        <div class="alert alert-warning" role="alert">
                                        <h2> Удачи! </h2>
                                        </div>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align="center"> Анкета претендента на участие в миссии </h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name = "surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name = "name"><br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="eduSelect"> Какое у вас образование? </label>
                                        <select class="form-control" id="eduSelect" name="edu">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div><br>
                                    <div> Какие у вас есть профессии? </div>
                                    <div class="form-group form-check">                 
                                        <input type="checkbox" class="form-check-input" id="opt1>
                                        <label class="form-check-label" for="opt1">инженер-исследователь</label>
                                    </div>
                                    <div class="form-group form-check">                 
                                        <input type="checkbox" class="form-check-input" id="opt2>
                                        <label class="form-check-label" for="opt2">инженер</label>
                                    </div>
                                    <div class="form-group form-check">                 
                                        <input type="checkbox" class="form-check-input" id="opt3>
                                        <label class="form-check-label" for="opt3">исследователь</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
