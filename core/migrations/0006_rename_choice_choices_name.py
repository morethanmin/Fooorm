# Generated by Django 3.2.5 on 2021-08-07 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210806_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choices',
            old_name='choice',
            new_name='name',
        ),
    ]
