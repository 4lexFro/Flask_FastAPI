from flask import Flask,render_template

app = Flask(__name__)

@app.route('/about/')
def about():
    context = {'content': 'Магазин "Эй,иди скорей!'}
    return render_template('about.html', **context)

if __name__ == '__main__':
    app.run()