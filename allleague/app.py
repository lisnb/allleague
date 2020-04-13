# coding:utf8

from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='../fe/dist')
app.debug = True

@app.route('/')
def index():
    print 'index'
    return app.send_static_file('index.html')


if __name__ == "__main__":
    from argparse import ArgumentParser
    argparser = ArgumentParser()
    argparser.add_argument('-p', '--port', default=80, type=int)
    args = argparser.parse_args()
    app.run('0.0.0.0', port=args.port)