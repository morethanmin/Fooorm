# Generated by Django 3.2.5 on 2021-08-07 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210808_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='responses',
            old_name='response_to',
            new_name='form',
        ),
        migrations.RenameField(
            model_name='responses',
            old_name='response_code',
            new_name='key',
        ),
        migrations.RemoveField(
            model_name='responses',
            name='responder_ip',
        ),
    ]
