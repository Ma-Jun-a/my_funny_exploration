from mycelery.makecelery import mycelery

app = mycelery(broker='redis://127.0.0.1:6379/1',bakend='redis://127.0.0.1:6379/2')
app.autodiscover_tasks('a')
