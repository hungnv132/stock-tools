from . import main


@main.route('/hello')
def index():
    return 'Hello Me!'
