# Generated by Django 2.1.4 on 2018-12-24 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='estado',
        ),
    ]