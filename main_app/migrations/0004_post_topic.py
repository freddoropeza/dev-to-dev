# Generated by Django 3.2.9 on 2021-11-23 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_topic_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.topic'),
            preserve_default=False,
        ),
    ]
