from celery import Celery

app = Celery(
    main="tasks",
    broker="pyamqp://guest@localhost//",
)


@app.task
def hello(name):
    message = f"Olá, {name}"
    return message
