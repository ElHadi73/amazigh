# Generated by Django 2.2.17 on 2020-12-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_auto_20201216_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='types',
            name='in_arabic',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='types',
            name='in_latine',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='types',
            name='in_tifinigh',
            field=models.CharField(max_length=20),
        ),
    ]
