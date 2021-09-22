import os
import flask_bootstrap
import flask
from flask import Flask
from flask import request
from flask import render_template


def site():
    os.mkdir(fname)
    os.chdir(os.getcwd() + '\\' + fname + '\\')
    os.mkdir(stdpath)
    os.chdir(os.getcwd() + '\\' + stdpath + '\\')

    @app.route('/')
    def ind():
        # return '<h1>MP</h1>'
        user_agent = request.headers.get('User-Agent')
        return '<p> Your brouser is %s</p>' % user_agent
        # return render_template('index.html')

    # print(os.getcwd())


if __name__ == '__main__':
    fname = str(input("рабочая папка"))

    stdpath = 'tamplates'
    app = Flask(__name__)
    site()
    app.run(debug=True)
