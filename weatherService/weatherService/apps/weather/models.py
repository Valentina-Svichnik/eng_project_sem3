from django.db import models

class Country(models.Model):
    name = models.CharField('название страны', max_length=100)
    popolation = models.CharField('население страны', max_length=100)
    square = models.CharField('площадь страны', max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    id_country = models.ForeignKey(Country, on_delete = models.CASCADE)

    name = models.CharField('название города', max_length=100)
    popolation = models.CharField('население города', max_length=100)
    square = models.CharField('площадь города', max_length=100)  

    def __str__(self):
        return self.name  

class District(models.Model):
    id_city = models.ForeignKey(City, on_delete = models.CASCADE)

    name = models.CharField('название района', max_length=100)
    popolation = models.CharField('население района', max_length=100)
    square = models.CharField('площадь района', max_length=100)    

    def __str__(self):
        return self.name

class Temperature (models.Model):
    id_district = models.IntegerField('id города')
    date = models.DateField('день')
    t_morning = models.IntegerField('температура утром')
    t_day = models.IntegerField('температура днем')
    t_evening = models.IntegerField('температура вечером')
    t_night = models.IntegerField('температура ночью')
    t_average = models.IntegerField('средняя температура за день')

    # def __str__(self):
    #     return (self.id_district, self.date)

class Humidity (models.Model):
    id_district = models.IntegerField('id города')
    date = models.DateField('день')
    h_morning = models.IntegerField('влажность утром')
    h_day = models.IntegerField('влажность днем')
    h_evening = models.IntegerField('влажность вечером')
    h_night = models.IntegerField('влажность ночью')
    h_average = models.IntegerField('средняя влажность за день')  

    # def __str__(self):
    #     return (self.id_district, self.date)

class Pressure (models.Model):
    id_district = models.IntegerField('id города')
    date = models.DateField('день')
    pressure_morning = models.IntegerField('давление утром')
    pressure_day = models.IntegerField('давление днем')
    pressure_evening = models.IntegerField('давление вечером')
    pressure_night = models.IntegerField('давление ночью')
    pressure_average = models.IntegerField('среднее давление за день')    

    # def __str__(self):
    #     return (self.id_district, self.date)

class Wind (models.Model):
    id_district = models.IntegerField('id города')
    date = models.DateField('день')
    w_morning = models.IntegerField('ветренность утром')
    w_day = models.IntegerField('ветренность днем')
    w_evening = models.IntegerField('ветренность вечером')
    w_night = models.IntegerField('ветренность ночью')
    w_average = models.IntegerField('средняя ветренность за день')   

    # def __str__(self):
    #     return (self.id_district, self.date)

class Precipitation (models.Model):
    id_district = models.IntegerField('id города')
    date = models.DateField('день')
    p_morning = models.IntegerField('количество осадков утром')
    p_name_morning = models.CharField('тип осадков утром', max_length=100)
    p_day = models.IntegerField('количество осадков днем')
    p_name_day = models.CharField('тип осадков днем', max_length=100)
    p_evening = models.IntegerField('количество осадков вечером')
    p_name_evening = models.CharField('тип осадков вечером', max_length=100)
    p_night = models.IntegerField('количество осадков ночью')
    p_name_night = models.CharField('тип осадков ночью', max_length=100)
    p_average = models.IntegerField('среднее количество осадков за день')  
    p_name_average = models.CharField('средний тип осадков за день', max_length=100)   

    # def __str__(self):
    #     return (self.id_district, self.date) 

class Precipitation_icon (models.Model):
    name = models.CharField('название типа осадков', max_length=100)
    icon = models.CharField('путь к иконке по типу осадков', max_length=100)  

    def __str__(self):
        return self.name 

class Cloud (models.Model):
    id_district = models.IntegerField('id города')
    date = models.DateField('день')
    c_morning = models.IntegerField('интенсивность облачности утром')
    c_name_morning = models.CharField('тип облачности утром', max_length=100)
    c_day = models.IntegerField('интенсивность облачности днем')
    c_name_day = models.CharField('тип облачности днем', max_length=100)
    c_evening = models.IntegerField('интенсивность облачности вечером')
    c_name_evening = models.CharField('тип облачности вечером', max_length=100)
    c_night = models.IntegerField('интенсивность облачности ночью')
    c_name_night = models.CharField('тип облачности ночью', max_length=100)
    c_average = models.IntegerField('средняя интенсивность облачности за день')  
    c_name_average = models.CharField('средний тип облачности за день', max_length=100)   

    # def __str__(self):
    #     return (self.id_district, self.date) 

class Cloudy_icon (models.Model):
    name = models.CharField('название типа облачности', max_length=100)
    icon = models.CharField('путь к иконке по типу облачности', max_length=100)

    # def __str__(self):
    #     return self.name

class New (models.Model):
    date = models.DateField('день')
    subject = models.CharField('тема новости', max_length=100)
    heading = models.TextField('заголовок новости')
    picture = models.CharField('путь к картинке', max_length=100)
    description = models.TextField('описание новости')
    source = models.CharField('источник новости', max_length=100)
    # def __str__(self):
    #     return (self.subject, self.heading) 

class Day(models.Model):
    id_district = models.ForeignKey(District, on_delete = models.CASCADE)
    date = models.DateField('день')
    news_id = models.ForeignKey(New, on_delete = models.CASCADE)
    id_temperature = models.ForeignKey(Temperature, on_delete = models.CASCADE)
    average_temperature = models.IntegerField('среднее значение температуры')
    id_humidity = models.ForeignKey(Humidity, on_delete = models.CASCADE)
    average_humidity = models.IntegerField('среднее значение влажности')
    id_precipitation = models.ForeignKey(Precipitation, on_delete = models.CASCADE)
    average_precipitation = models.IntegerField('среднее значение осадков')
    name_precipitation = models.CharField('средний тип осадков', max_length=100) 
    icon_precipitation = models.CharField('путь к иконке по типу осадков', max_length=100)  
    id_cloud = models.ForeignKey(Cloud, on_delete = models.CASCADE)
    average_cloud = models.IntegerField('среднее значение облачности')
    name_cloud = models.CharField('средний тип облачности', max_length=100) 
    icon_cloud = models.CharField('путь к иконке по типу облачности', max_length=100)  
    id_pressure = models.ForeignKey(Pressure, on_delete = models.CASCADE)
    average_pressure = models.IntegerField('среднее значение давления')
    id_wind = models.ForeignKey(Wind, on_delete = models.CASCADE)
    average_wind = models.IntegerField('среднее значение ветренности')

    # def __str__(self):
    #     return (self.id_district, self.date) 


class User(models.Model):
    type = models.IntegerField('тип пользователя')
    name = models.CharField('имя пользователя', max_length=100)
    surname = models.CharField('фамилия пользователя', max_length=100)
    patronymic = models.CharField('отчество пользователя', max_length=100)
    male = models.CharField('гендер пользователя', max_length=1)
    email = models.CharField('email пользователя', max_length=100)
    birthday = models.DateField('день рождения пользователя')
    login = models.CharField('логин пользователя', max_length=100)
    password = models.CharField('пароль пользователя', max_length=100)

    # def __str__(self):
    #     return (self.name) 

class Advertice (models.Model):
    subject = models.CharField('тема рекламного объявления', max_length=100)
    heading = models.TextField('заголовок рекламного объявления')
    picture = models.CharField('путь к картинке', max_length=100)
    description = models.TextField('описание рекламного объявления')
    firm_name = models.CharField('рекламируемая фирма', max_length=100)

    def __str__(self):
        return (self.subject, self.heading, self.firm_name) 
    