from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Dariia!"


@app.route('/hello')
def hello():
    return 'Hi there!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
