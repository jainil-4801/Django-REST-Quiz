# Generated by Django 3.1.2 on 2020-10-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0009_auto_20201017_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersanswer',
            name='text_ans',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]