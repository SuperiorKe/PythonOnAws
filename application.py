"""Module providing a function display text on '/'."""
from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    """Function serving the text."""
    return 'Sup. Subscribe'

if __name__ == '__main__':
    application.run(debug=True)
    