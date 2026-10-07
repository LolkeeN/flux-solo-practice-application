from flask import Flask

app = Flask(__name__)

with open("VERSION", "r") as f:
    VERSION = f.read().strip()


@app.route("/", methods=["GET"])
def hello():
    return f"Hello World! v{VERSION}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
