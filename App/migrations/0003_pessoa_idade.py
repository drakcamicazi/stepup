# Generated by Django 2.1.3 on 2018-11-20 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_remove_pessoa_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='idade',
            field=models.PositiveIntegerField(default=18),
        ),
    ]