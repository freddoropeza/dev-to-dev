# Generated by Django 3.2.9 on 2021-11-23 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20211123_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='date_published'),
        ),
    ]