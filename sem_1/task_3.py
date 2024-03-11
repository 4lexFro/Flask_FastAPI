# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.

from flask import Flask

app = Flask(__name__)

@app.route('/str_ing/<my_str>/')
def text_length(my_str):
    return str(len(my_str))

if __name__ == '__main__':
    app.run()
