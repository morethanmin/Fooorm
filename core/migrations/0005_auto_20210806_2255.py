# Generated by Django 3.2.5 on 2021-08-06 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210806_2245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='question_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='question_type',
            new_name='type',
        ),
    ]
