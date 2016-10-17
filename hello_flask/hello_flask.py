#!usr/bin/env python

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    """ Displays the index page
    """
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

