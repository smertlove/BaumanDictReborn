# Generated by Django 3.2.9 on 2021-11-24 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, verbose_name='eng word')),
                ('translation', models.CharField(max_length=100, verbose_name='ru translation')),
                ('transcription', models.CharField(max_length=50, verbose_name='eng transcription')),
                ('pos', models.CharField(max_length=5, verbose_name='part of speech')),
                ('eng_example', models.CharField(max_length=250, verbose_name='eng example sentence')),
                ('ru_example', models.CharField(max_length=250, verbose_name='ru example sentence')),
                ('module', models.IntegerField(verbose_name='module')),
            ],
        ),
    ]