# Generated by Django 4.0.4 on 2022-05-18 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='_is_displayed',
            field=models.BooleanField(default=True, verbose_name='Is displayed'),
        ),
    ]
