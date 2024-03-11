# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# 📌Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# 📌Данные о студентах должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

app = Flask(__name__)

_users = [{'name': 'Иван', 'last_name': 'Иванов',
           'age': '44', 'average_mark': '4.8',},
          {'name': 'Петр', 'last_name': 'Семенов',
           'age': '35', 'average_mark': '3.3',},
          ]

@app.route('/table/')
def table():
    return render_template ('table.html',users = _users)



if __name__ == '__main__':
    app.run()