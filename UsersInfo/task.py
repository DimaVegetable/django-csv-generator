from DataUsers.celery import app
from .models import Schema


@app.task
def generator_form():
    Schema.objects.create(name_schema='fake', first_name='Dima', last_name='Motrii', phone_number=380978939068, email='asdasd@ukr.net',
                          job='asdfdsfa', company='asdcxv', address='asdxcvgfdsgdfgdfherwt', age=16)
