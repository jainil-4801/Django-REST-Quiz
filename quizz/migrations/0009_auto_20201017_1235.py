# Generated by Django 3.1.2 on 2020-10-17 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0008_question_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='options',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
