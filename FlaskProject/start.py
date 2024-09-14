from flask import Flask

app = Flask(__name__)




@app.route("/")
def index():
    return "Hello World!"


@app.route("/<name>")
def nmae_changer(name=None):
    if name is None:
        return "Ты кто"
        return f"О, привет, {name}"

@app.route("/main")
def hello():
    html = """
    <head><title>Главная страница</title></head>
    <body>
        <h1>Привет</h1>
    </body>
    """
    return html


if __name__ == "__main__":
    app.run()
