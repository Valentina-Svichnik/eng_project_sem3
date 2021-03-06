# Generated by Django 3.1.5 on 2021-01-09 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_district', models.IntegerField(verbose_name='id города')),
                ('date', models.DateField(verbose_name='день')),
                ('c_morning', models.IntegerField(verbose_name='интенсивность облачности утром')),
                ('c_name_morning', models.CharField(max_length=100, verbose_name='тип облачности утром')),
                ('c_day', models.IntegerField(verbose_name='интенсивность облачности днем')),
                ('c_name_day', models.CharField(max_length=100, verbose_name='тип облачности днем')),
                ('c_evening', models.IntegerField(verbose_name='интенсивность облачности вечером')),
                ('c_name_evening', models.CharField(max_length=100, verbose_name='тип облачности вечером')),
                ('c_night', models.IntegerField(verbose_name='интенсивность облачности ночью')),
                ('c_name_night', models.CharField(max_length=100, verbose_name='тип облачности ночью')),
                ('c_average', models.IntegerField(verbose_name='средняя интенсивность облачности за день')),
                ('c_name_average', models.CharField(max_length=100, verbose_name='средний тип облачности за день')),
            ],
        ),
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(verbose_name='день'),
        ),
        migrations.AlterField(
            model_name='humidity',
            name='date',
            field=models.DateField(verbose_name='день'),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(verbose_name='день'),
        ),
        migrations.AlterField(
            model_name='precipitation',
            name='date',
            field=models.DateField(verbose_name='день'),
        ),
        migrations.AlterField(
            model_name='pressure',
            name='date',
            field=models.DateField(verbose_name='день'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='date',
            field=models.DateField(verbose_name='день'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(verbose_name='день рождения пользователя'),
        ),
        migrations.AlterField(
            model_name='wind',
            name='date',
            field=models.DateField(verbose_name='день'),
        ),
        migrations.AlterField(
            model_name='day',
            name='id_cloud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.cloud'),
        ),
        migrations.DeleteModel(
            name='Cloudy',
        ),
    ]
