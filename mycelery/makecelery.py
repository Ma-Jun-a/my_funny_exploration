from celery import Celery

# class mycelery(Celery):
#
#     def gen_task_name(self, name, module):
#         if module.endswith('.task'):
#             module = module[:-5]
#         return super(mycelery, self).gen_task_name(name, module)
def make_celery(app):
    celery = Celery(app.import_name,broker=app.config['CELERY_BROKER_URL'],bakend=app.config['CELERY_BACKEND'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContestTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self,*args,**kwargs)
    celery.Task = ContestTask
    return celery

