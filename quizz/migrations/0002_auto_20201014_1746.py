# Generated by Django 3.1.2 on 2020-10-14 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
