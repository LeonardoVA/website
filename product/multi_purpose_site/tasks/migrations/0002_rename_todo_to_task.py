# Generated by Django 2.0.5 on 2018-06-11 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='todo_entries',
            new_name='Tasks',
        ),
    ]
