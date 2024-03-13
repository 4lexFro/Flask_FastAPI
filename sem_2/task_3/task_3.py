# 📌Создать страницу, на которой будет форма для ввода логина
# и пароля
# 📌При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.

from pathlib import PurePath, Path
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

LOGIN = 'admin'
PASSWORD = '1234'

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method=='GET ':
        return render_template ('login.html')
    get_login = request.form.get('login')
    get_password = request.form.get('password')

    if get_login == LOGIN and get_password == PASSWORD:
        return render_template('index.html')
    return render_template('error.html')





if __name__ == '__main__':
    app.run()