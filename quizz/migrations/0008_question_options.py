# Generated by Django 3.1.2 on 2020-10-17 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0007_auto_20201016_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]