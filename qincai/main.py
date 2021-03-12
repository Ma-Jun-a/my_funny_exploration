import time模块

from celery import Celery

# app = Celery('fskjf',broker= 'redis://python:chuanzhi@192.168.30.132:6379/1',backend= 'redis://python:chuanzhi@192.168.30.132:6379/2')
app = Celery('fskjf',broker= 'redis://127.0.0.1:6379/1',backend= 'redis://127.0.0.1:6379/2')

# app.config_from_object()
@app.task
def reverse(string):
    time模块.sleep(0.1)
    return string[::-1]
if __name__ == '__main__':
    app.run('majun')

