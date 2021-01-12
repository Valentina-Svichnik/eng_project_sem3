from django.db import models

class Advertice (models.Model):
    subject = models.CharField('тема рекламного объявления', max_length=100)
    heading = models.TextField('заголовок рекламного объявления')
    picture = models.CharField('путь к картинке', max_length=100)
    description = models.TextField('описание рекламного объявления')
    firm_name = models.CharField('рекламируемая фирма', max_length=100)

    def __str__(self):
        return (self.subject) 

class New (models.Model):
    date = models.DateField('день')
    subject = models.CharField('тема новости', max_length=100)
    heading = models.TextField('заголовок новости')
    picture = models.CharField('путь к картинке', max_length=100)
    description = models.TextField('описание новости')
    source = models.CharField('источник новости', max_length=100)

    def __str__(self):
        return (self.subject)    
