from jinja2 import Template
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_page():
    variables = {
        "title": "MyPythonProject",
        "name": "Вакиль",
        "nickname": "Польша",

    }
    food = {
        "shaurma": ["Шаурму", "А кто то её не любит?", "static/image/shaurma.jpg"],
        "pizza": ["Пицу", "На ней такой вкусный и тягучий сыр что дальше даже не стоит обьяснять", "static/image/pizza.jpg"],
        "chicken_gril": ["Курица гриль", "она сочная вкусная, она завернута в лаваш и вообще курица гриль onelove", "static/image/chicken_gril.jpg"],
        "naggets": ["Нагетцы", "gedagedigedagedago", "static/image/naggets.jpg"],
    }

    return render_template("aboba.html", **variables, food=food)


if __name__ == "__main__":
    app.run()
