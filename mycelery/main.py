import time模块

from flask import Flask

from mycelery.makecelery import make_celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://127.0.0.1:6379/1'
app.config['CELERY_BACKEND'] = 'redis://127.0.0.1:6379/2'

celery = make_celery(app)

@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return 'I send an async request'
@celery.task(name='main.reverse')
def reverse(string):
    # time.sleep(10)
    return string[::-1]
if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1')

