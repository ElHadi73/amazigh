# Generated by Django 2.2.17 on 2020-12-16 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_amazigh', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_arabic', models.CharField(max_length=20)),
                ('in_latine', models.CharField(max_length=20)),
                ('in_tifinigh', models.CharField(max_length=20)),
                ('many_means', models.ManyToManyField(blank=True, null=True, related_name='_word_many_means_+', to='words.Word')),
                ('opst_words', models.ManyToManyField(blank=True, null=True, related_name='_word_opst_words_+', to='words.Word')),
                ('racine_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='words.Word')),
                ('type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='words.Types')),
            ],
        ),
        migrations.CreateModel(
            name='Types_translations',
            fields=[
                ('translation', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('lang_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='words.Languages')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='words.Types')),
            ],
        ),
        migrations.CreateModel(
            name='translations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traduction', models.CharField(max_length=20)),
                ('Description', models.CharField(blank=True, max_length=200, null=True)),
                ('ama_words', models.ManyToManyField(to='words.Word')),
                ('lang_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='words.Languages')),
            ],
        ),
    ]