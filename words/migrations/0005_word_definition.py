# Generated by Django 2.2.17 on 2020-12-20 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0004_auto_20201216_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='Definition',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
