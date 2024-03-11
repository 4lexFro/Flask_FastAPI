# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# 📌Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# 📌Данные о новостях должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

app = Flask(__name__)

_news = [{'title': 'main_news', 'content': 'А лисички взяли спички',
           'date': '10.03.2024',},
          {'title': 'other_news', 'content': 'А слониха,вся дрожа,так и села на ежа',
           'date': '8.03.2024',},]

@app.route('/news/')
def news():
    return render_template ('news.html',news = _news)



if __name__ == '__main__':
    app.run()