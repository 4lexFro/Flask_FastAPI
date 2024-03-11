from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    context = {'content': 'Магазин "Эй,иди скорей!'}
    return render_template('main_page.html', **context)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.route('/clothes/')
def clothes():
    context = {'content': 'Линейка одежды от Надежды'}
    return render_template('clothes.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'content': 'Обувь от Abibas'}
    return render_template('shoes.html', **context)


@app.route('/clothes/jacket/')
def jacket():
    context = {'content': 'Куртки от Vazгена'}
    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run()
