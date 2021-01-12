from django.db import models

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

    def __str__(self):
        return (self.name, self.surname, self.patronymic)      
