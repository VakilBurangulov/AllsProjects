from flask import Flask, render_template

app = Flask(__name__)

image = {
    "logo": "../static/image/logo.png"
}
capabilitie = [{
    "title": "Написать телеграм бота на PyTelegramBotApi",
    "image": "../static/image/tg_bot.png"},
    {
    "title": "Написать сайт на Flask как этот",
    "image": "../static/image/site.png"},
    {
    "title": 'Написать игру на PyGame',
    "image": "../static/image/pygame.png"},
]

href = {
    "index": '/',
    "no_money": '/no-money',
    "capabilities": '/capabilities',
    "contacts": '/contacts',
}
contact = [
        {
                "title": 'Телефон',
                "info": '+79672825004'
        },
        {
                "title": 'E-mail',
                "info": 'burangulov.vakil@gmail.com'
        },
        {
                "title": 'Телеграм',
                "info": '@Burangulov_Vakil'
        }
]


@app.route('/')
def index():
    return render_template('index.html', page_index='index', page_name='Главная', **href, **image)


@app.route("/contacts")
def contacts():
        context = {"contact": contact}
        return render_template("contacts.html", page_index='contacts', **image, **href, page_name='Контакты',  **context)


@app.route('/capabilities')
def capabilities():
    context = {"capabilitie": capabilitie}

    return render_template('capabilities.html', page_index='capabilities', page_name='Мои умения', **href, **context, **image)


@app.route("/no-money")
def no_money():
    food = {
        "shaurma": ["Шаурму", "А кто то её не любит?", "static/image/shaurma.jpg"],
        "pizza": ["Пицу", "На ней такой вкусный и тягучий сыр что дальше даже не стоит обьяснять", "static/image/pizza.jpg"],
        "chicken_gril": ["Курица гриль", "она сочная вкусная, она завернута в лаваш и вообще курица гриль onelove", "static/image/chicken_gril.jpg"],
        "naggets": ["Нагетцы", "gedagedigedagedago", "static/image/naggets.jpg"],
    }

    return render_template("no-money.html", food=food, **href, page_index='no_money', page_name='Работа за еду', **image)


if __name__ == "__main__":
    app.run()
