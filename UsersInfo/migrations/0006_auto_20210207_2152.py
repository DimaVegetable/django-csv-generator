# Generated by Django 3.1.6 on 2021-02-07 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersInfo', '0005_auto_20210207_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
