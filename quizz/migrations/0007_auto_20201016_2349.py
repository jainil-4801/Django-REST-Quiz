# Generated by Django 3.1.2 on 2020-10-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0006_usersanswer_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='quiz/images'),
        ),
    ]
