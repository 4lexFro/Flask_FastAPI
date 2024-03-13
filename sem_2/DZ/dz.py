# Создать страницу, на которой будет форма для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя, а также
# будет произведено перенаправление на страницу приветствия, где будет отображаться
# имя пользователя.На странице приветствия должна быть кнопка «Выйти», при нажатии
# на которую будет удалён cookie-файл с данными пользователя и произведено
# перенаправление на страницу ввода имени и электронной почты.


from flask import Flask, request, make_response, render_template, redirect, url_for

app=Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/cookie/', methods=['POST'])
def cookie():
    username = request.form['name']
    usermail = request.form['mail']
    response = make_response(redirect('/hello/'))
    response.set_cookie('name', username)
    response.set_cookie('mail', usermail)
    return response


@app.route('/hello/')
def hello():
    username = request.cookies.get('name')
    usermail = request.cookies.get('mail')
    if not username or not usermail:
        return redirect(url_for('login'))
    return render_template('hello.html', name=username)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('name')
        usermail = request.form.get('mail')
        context = {'username': username,
                   'usermail': usermail}
    return render_template('login.html')


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('name')
    response.delete_cookie('mail')
    return response


if __name__ == '__main__':
    app.run(debug=True)