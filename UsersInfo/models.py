from django.db import models
from django.utils import timezone


class Schema(models.Model):
    id = models.AutoField(primary_key=True)
    name_schema = models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=40, null=True)
    last_name = models.CharField(max_length=40, null=True)
    phone_number = models.IntegerField(null=True)
    email = models.EmailField(null=True, max_length=250)
    job = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=200, null=True)
    address = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name_schema

    def get_absolute_url(self):
        return f'/home'