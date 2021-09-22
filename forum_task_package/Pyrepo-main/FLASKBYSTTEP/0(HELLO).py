from flask import Flask

app = Flask(__name__)


@app.route('/')
def ind():
    return '<h1>MP</h1>'


if __name__ == '__main__':
    app.run(debug=True)
