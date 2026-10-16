from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return f"Hello World! From knowledge sharing project x3"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
