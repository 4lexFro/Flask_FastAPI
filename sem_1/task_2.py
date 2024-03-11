# 📌Дорабатываем задачу 1.
# 📌Добавьте две дополнительные страницы в ваше веб-
# приложение:
# ○страницу "about"
# ○страницу "contact".
# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/about/')
def about_html():
    return ('about.html')


@app.route('/contact/')
def contact_html():
    return ('contact.html')


@app.route('/number/<int:num1>/<int:num2>/')
def sum_nums(num1, num2):
    return str(num1 + num2)


if __name__ == '__main__':
    app.run()
