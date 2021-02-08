# Generated by Django 3.1.6 on 2021-02-07 21:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UsersInfo', '0003_auto_20210207_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='schema',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='schema',
            name='age',
            field=models.IntegerField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='schema',
            name='company',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='schema',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='schema',
            name='email',
            field=models.EmailField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='schema',
            name='job',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='schema',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='schema',
            name='first_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='schema',
            name='last_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='schema',
            name='name_schema',
            field=models.CharField(max_length=30, null=True),
        ),
    ]