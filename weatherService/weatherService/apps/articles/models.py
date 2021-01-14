from django.db import models

class Advertice (models.Model):
    subject = models.CharField('Subject', max_length=100)
    heading = models.TextField('Heading')
    picture = models.CharField('Way to the picture', max_length=100)
    description = models.TextField('Description')
    firm_name = models.CharField('Name of the firm', max_length=100)

    def __str__(self):
        return (self.subject) 

class New (models.Model):
    date = models.DateField('Date')
    subject = models.CharField('Subject of the News', max_length=100)
    heading = models.TextField('Heading')
    picture = models.CharField('Way to the picture', max_length=100)
    description = models.TextField('Description')
    source = models.CharField('Source', max_length=100)

    def __str__(self):
        return (self.subject)    
