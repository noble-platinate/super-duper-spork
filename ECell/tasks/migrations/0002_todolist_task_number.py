# Generated by Django 3.2.3 on 2021-05-17 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='task_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
