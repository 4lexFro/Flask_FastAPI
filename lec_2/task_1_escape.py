from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'

@app.route('/<path:file>/')
def get_file(file):
    print(file)
    #return f'Ваш файл находится в: {file}!'
    return f'Ваш файл находится в: {escape(file)}!' # escape не позволяет запустится скрипту,
#а выводит в текстовом виде


if __name__ == '__main__':
    app.run()