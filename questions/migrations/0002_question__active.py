# Generated by Django 2.1.7 on 2019-07-03 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='_active',
            field=models.BooleanField(default=False),
        ),
    ]