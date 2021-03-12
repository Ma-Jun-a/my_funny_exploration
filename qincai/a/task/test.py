from mycelery.main import app


@app.task
def func():
    return 'task1'
