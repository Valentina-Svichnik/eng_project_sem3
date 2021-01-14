from django.db import models

class Country(models.Model):
    name = models.CharField('Name of the country', max_length=100)
    popolation = models.CharField('Population', max_length=100)
    square = models.CharField('Square', max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    id_country = models.ForeignKey(Country, on_delete = models.CASCADE)

    name = models.CharField('Name of the city', max_length=100)
    popolation = models.CharField('Population', max_length=100)
    square = models.CharField('Square', max_length=100)  

    def __str__(self):
        return self.name  

class District(models.Model):
    id_city = models.ForeignKey(City, on_delete = models.CASCADE)

    name = models.CharField('Name of the district', max_length=100)
    popolation = models.CharField('Population', max_length=100)
    square = models.CharField('Square', max_length=100)    

    def __str__(self):
        return self.name

class Temperature (models.Model):
    id_district = models.IntegerField('id of the district')
    date = models.DateField('Day')
    t_morning = models.IntegerField('Temperature in the morning')
    t_day = models.IntegerField('Temperature at the day')
    t_evening = models.IntegerField('Temperature in the evening')
    t_night = models.IntegerField('Temperature at the night')
    t_average = models.IntegerField('Average temperature', null=True)


class Humidity (models.Model):
    id_district = models.IntegerField('id of the district')
    date = models.DateField('day')
    h_morning = models.IntegerField('Humidity in the morning')
    h_day = models.IntegerField('Humidity at the day')
    h_evening = models.IntegerField('Humidity in the evening')
    h_night = models.IntegerField('Humidity at the night')
    h_average = models.IntegerField('Average humidity')  


class Pressure (models.Model):
    id_district = models.IntegerField('id of the district')
    date = models.DateField('day')
    pressure_morning = models.IntegerField('Pressure in the morning')
    pressure_day = models.IntegerField('Pressure at the day')
    pressure_evening = models.IntegerField('Pressure in the evening')
    pressure_night = models.IntegerField('Pressure at the night')
    pressure_average = models.IntegerField('Average pressure')    


class Wind (models.Model):
    id_district = models.IntegerField('id of the district')
    date = models.DateField('day')
    w_morning = models.IntegerField('Wind in the morning')
    w_day = models.IntegerField('Wind at the day')
    w_evening = models.IntegerField('Wind in the evening')
    w_night = models.IntegerField('Wind at the night')
    w_average = models.IntegerField('Average wind')   


class Precipitation (models.Model):
    id_district = models.IntegerField('id of the district')
    date = models.DateField('day')
    p_morning = models.IntegerField('The quality of precipitation in the morning')
    p_name_morning = models.CharField('The type of precipitation in the morning', max_length=100)
    p_day = models.IntegerField('The quality of precipitation at the day')
    p_name_day = models.CharField('The type of precipitation at the day', max_length=100)
    p_evening = models.IntegerField('The quality of precipitation in the evening')
    p_name_evening = models.CharField('The type of precipitation in the evening', max_length=100)
    p_night = models.IntegerField('The quality of precipitation at the night')
    p_name_night = models.CharField('The type of precipitation at the night', max_length=100)
    p_average = models.IntegerField('The average quality of precipitation')  
    p_name_average = models.CharField('the average type of precipitation', max_length=100)   


class Precipitation_icon (models.Model):
    name = models.CharField('The name of precipitation', max_length=100)
    icon = models.CharField('The way to the icon', max_length=100)  


class Cloud (models.Model):
    id_district = models.IntegerField('id of the district')
    date = models.DateField('day')
    c_morning = models.IntegerField('The intensity od clouds in the morning')
    c_name_morning = models.CharField('The type of clouds in the morning', max_length=100)
    c_day = models.IntegerField('The intensity od clouds at the day')
    c_name_day = models.CharField('The type of clouds at the day', max_length=100)
    c_evening = models.IntegerField('The intensity od clouds in the evening')
    c_name_evening = models.CharField('The type of clouds in the evening', max_length=100)
    c_night = models.IntegerField('The intensity od clouds at the night')
    c_name_night = models.CharField('The type of clouds at the night', max_length=100)
    c_average = models.IntegerField('The average intensity od clouds')  
    c_name_average = models.CharField('The average type of clouds', max_length=100)   


class Cloudy_icon (models.Model):
    name = models.CharField('The name of clouds', max_length=100)
    icon = models.CharField('The way to the icon', max_length=100)


class Day(models.Model):
    id_district = models.ForeignKey(District, on_delete = models.CASCADE)
    date = models.DateField('day')
    id_temperature = models.ForeignKey(Temperature, on_delete = models.CASCADE)
    average_temperature = models.IntegerField('Average temperature')
    id_humidity = models.ForeignKey(Humidity, on_delete = models.CASCADE)
    average_humidity = models.IntegerField('Average humidity')
    id_precipitation = models.ForeignKey(Precipitation, on_delete = models.CASCADE)
    average_precipitation = models.IntegerField('the average type of precipitation')
    name_precipitation = models.CharField('The name of precipitation', max_length=100) 
    icon_precipitation = models.CharField('The way to the icon of precipitation', max_length=100)  
    id_cloud = models.ForeignKey(Cloud, on_delete = models.CASCADE)
    average_cloud = models.IntegerField('The average intensity od clouds')
    name_cloud = models.CharField('The average type of clouds', max_length=100) 
    icon_cloud = models.CharField('The way to the icon of cloud', max_length=100)  
    id_pressure = models.ForeignKey(Pressure, on_delete = models.CASCADE)
    average_pressure = models.IntegerField('Average pressure')
    id_wind = models.ForeignKey(Wind, on_delete = models.CASCADE)
    average_wind = models.IntegerField('Average wind')
