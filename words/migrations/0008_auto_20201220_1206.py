# Generated by Django 2.2.17 on 2020-12-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0007_auto_20201220_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='many_means',
            field=models.ManyToManyField(related_name='_word_many_means_+', to='words.Word'),
        ),
        migrations.AlterField(
            model_name='word',
            name='opst_words',
            field=models.ManyToManyField(related_name='_word_opst_words_+', to='words.Word'),
        ),
    ]
