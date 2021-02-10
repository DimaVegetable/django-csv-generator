from DataUsers.celery import app


@app.task
def generator_form():
    pass
