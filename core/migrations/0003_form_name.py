# Generated by Django 3.2.5 on 2021-08-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210806_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='name',
            field=models.CharField(default='새로운 타이틀', max_length=200),
            preserve_default=False,
        ),
    ]
