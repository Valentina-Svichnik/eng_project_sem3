# Generated by Django 3.1.5 on 2021-01-09 16:03

from django.db import migrations, models
import django.db.models.deletion


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
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название города')),
                ('popolation', models.CharField(max_length=100, verbose_name='население города')),
                ('square', models.CharField(max_length=100, verbose_name='площадь города')),
            ],
        ),
        migrations.CreateModel(
            name='Cloudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_district', models.IntegerField(verbose_name='id города')),
                ('date', models.DateTimeField(verbose_name='день')),
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
        migrations.CreateModel(
            name='Cloudy_icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название типа облачности')),
                ('icon', models.CharField(max_length=100, verbose_name='путь к иконке по типу облачности')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название страны')),
                ('popolation', models.CharField(max_length=100, verbose_name='население страны')),
                ('square', models.CharField(max_length=100, verbose_name='площадь страны')),
            ],
        ),
        migrations.CreateModel(
            name='Humidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_district', models.IntegerField(verbose_name='id города')),
                ('date', models.DateTimeField(verbose_name='день')),
                ('h_morning', models.IntegerField(verbose_name='влажность утром')),
                ('h_day', models.IntegerField(verbose_name='влажность днем')),
                ('h_evening', models.IntegerField(verbose_name='влажность вечером')),
                ('h_night', models.IntegerField(verbose_name='влажность ночью')),
                ('h_average', models.IntegerField(verbose_name='средняя влажность за день')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='день')),
                ('subject', models.CharField(max_length=100, verbose_name='тема новости')),
                ('heading', models.TextField(verbose_name='заголовок новости')),
                ('picture', models.CharField(max_length=100, verbose_name='путь к картинке')),
                ('description', models.TextField(verbose_name='описание новости')),
                ('source', models.CharField(max_length=100, verbose_name='источник новости')),
            ],
        ),
        migrations.CreateModel(
            name='Precipitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_district', models.IntegerField(verbose_name='id города')),
                ('date', models.DateTimeField(verbose_name='день')),
                ('p_morning', models.IntegerField(verbose_name='количество осадков утром')),
                ('p_name_morning', models.CharField(max_length=100, verbose_name='тип осадков утром')),
                ('p_day', models.IntegerField(verbose_name='количество осадков днем')),
                ('p_name_day', models.CharField(max_length=100, verbose_name='тип осадков днем')),
                ('p_evening', models.IntegerField(verbose_name='количество осадков вечером')),
                ('p_name_evening', models.CharField(max_length=100, verbose_name='тип осадков вечером')),
                ('p_night', models.IntegerField(verbose_name='количество осадков ночью')),
                ('p_name_night', models.CharField(max_length=100, verbose_name='тип осадков ночью')),
                ('p_average', models.IntegerField(verbose_name='среднее количество осадков за день')),
                ('p_name_average', models.CharField(max_length=100, verbose_name='средний тип осадков за день')),
            ],
        ),
        migrations.CreateModel(
            name='Precipitation_icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название типа осадков')),
                ('icon', models.CharField(max_length=100, verbose_name='путь к иконке по типу осадков')),
            ],
        ),
        migrations.CreateModel(
            name='Pressure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_district', models.IntegerField(verbose_name='id города')),
                ('date', models.DateTimeField(verbose_name='день')),
                ('pressure_morning', models.IntegerField(verbose_name='давление утром')),
                ('pressure_day', models.IntegerField(verbose_name='давление днем')),
                ('pressure_evening', models.IntegerField(verbose_name='давление вечером')),
                ('pressure_night', models.IntegerField(verbose_name='давление ночью')),
                ('pressure_average', models.IntegerField(verbose_name='среднее давление за день')),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_district', models.IntegerField(verbose_name='id города')),
                ('date', models.DateTimeField(verbose_name='день')),
                ('t_morning', models.IntegerField(verbose_name='температура утром')),
                ('t_day', models.IntegerField(verbose_name='температура днем')),
                ('t_evening', models.IntegerField(verbose_name='температура вечером')),
                ('t_night', models.IntegerField(verbose_name='температура ночью')),
                ('t_average', models.IntegerField(verbose_name='средняя температура за день')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(verbose_name='тип пользователя')),
                ('name', models.CharField(max_length=100, verbose_name='имя пользователя')),
                ('surname', models.CharField(max_length=100, verbose_name='фамилия пользователя')),
                ('patronymic', models.CharField(max_length=100, verbose_name='отчество пользователя')),
                ('male', models.CharField(max_length=1, verbose_name='гендер пользователя')),
                ('email', models.CharField(max_length=100, verbose_name='email пользователя')),
                ('birthday', models.DateTimeField(verbose_name='день рождения пользователя')),
                ('login', models.CharField(max_length=100, verbose_name='логин пользователя')),
                ('password', models.CharField(max_length=100, verbose_name='пароль пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='Wind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_district', models.IntegerField(verbose_name='id города')),
                ('date', models.DateTimeField(verbose_name='день')),
                ('w_morning', models.IntegerField(verbose_name='ветренность утром')),
                ('w_day', models.IntegerField(verbose_name='ветренность днем')),
                ('w_evening', models.IntegerField(verbose_name='ветренность вечером')),
                ('w_night', models.IntegerField(verbose_name='ветренность ночью')),
                ('w_average', models.IntegerField(verbose_name='средняя ветренность за день')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название района')),
                ('popolation', models.CharField(max_length=100, verbose_name='население района')),
                ('square', models.CharField(max_length=100, verbose_name='площадь района')),
                ('id_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.city')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='день')),
                ('average_temperature', models.IntegerField(verbose_name='среднее значение температуры')),
                ('average_humidity', models.IntegerField(verbose_name='среднее значение влажности')),
                ('average_precipitation', models.IntegerField(verbose_name='среднее значение осадков')),
                ('name_precipitation', models.CharField(max_length=100, verbose_name='средний тип осадков')),
                ('icon_precipitation', models.CharField(max_length=100, verbose_name='путь к иконке по типу осадков')),
                ('average_cloud', models.IntegerField(verbose_name='среднее значение облачности')),
                ('name_cloud', models.CharField(max_length=100, verbose_name='средний тип облачности')),
                ('icon_cloud', models.CharField(max_length=100, verbose_name='путь к иконке по типу облачности')),
                ('average_pressure', models.IntegerField(verbose_name='среднее значение давления')),
                ('average_wind', models.IntegerField(verbose_name='среднее значение ветренности')),
                ('id_cloud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.cloudy')),
                ('id_district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.district')),
                ('id_humidity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.humidity')),
                ('id_precipitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.precipitation')),
                ('id_pressure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.pressure')),
                ('id_temperature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.temperature')),
                ('id_wind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.wind')),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.new')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='id_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.country'),
        ),
    ]
