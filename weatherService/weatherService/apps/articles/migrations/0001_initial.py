# Generated by Django 3.1.5 on 2021-01-12 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='тема рекламного объявления')),
                ('heading', models.TextField(verbose_name='заголовок рекламного объявления')),
                ('picture', models.CharField(max_length=100, verbose_name='путь к картинке')),
                ('description', models.TextField(verbose_name='описание рекламного объявления')),
                ('firm_name', models.CharField(max_length=100, verbose_name='рекламируемая фирма')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='день')),
                ('subject', models.CharField(max_length=100, verbose_name='тема новости')),
                ('heading', models.TextField(verbose_name='заголовок новости')),
                ('picture', models.CharField(max_length=100, verbose_name='путь к картинке')),
                ('description', models.TextField(verbose_name='описание новости')),
                ('source', models.CharField(max_length=100, verbose_name='источник новости')),
            ],
        ),
    ]
