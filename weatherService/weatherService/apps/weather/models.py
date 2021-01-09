import datetime
from django.db import models

class Weather(models.Model):
    weather_title = models.CharField('название', max_length = 200)
    weather_text = models.TextField('текст')
    date = models.DateTimeField('дата')

    def __str__(self):
        return self.weather_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):    
    article = models.ForeignKey(Weather, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.TextField('комментарий')

    def __str__(self):
        return self.author_name