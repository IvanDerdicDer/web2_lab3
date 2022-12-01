from os import environ as env
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html')


if __name__ == '__main__':
    url = env.get("RENDER_EXTERNAL_URL")
    port = env.get('PORT')

    if url:
        url = '127.0.0.1'

    if port:
        port = int(port)

    if not url:
        url = None

    if not port:
        port = None

    app.run(host=url, port=port)
