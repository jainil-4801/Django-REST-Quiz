# Generated by Django 3.1.2 on 2020-10-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0002_auto_20201014_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
