from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", x="Hallo Mirco!")


if __name__ == '__main__':
    app.run(port=1337, debug=True)
