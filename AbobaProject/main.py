from flask import Flask, render_template
import datetime
app = Flask(__name__)

# year = datetime.datetime.year.
@app.route('/')
def index():
    context = {
        'title': 'Главная',
        'page': 'index'
    }
    return render_template('index.html', **context)

@app.route('/blog/')
def blog():
    context = {
        'title': 'Блог',
        'page': 'blog'
    }
    return render_template('blog.html', **context)

@app.route('/contacts/')
def contacts():
    context = {
        'title': 'Контакты',
        'page': 'contacts'
    }
    return render_template('contacts.html', **context)


if __name__ == '__main__':
    app.run()
