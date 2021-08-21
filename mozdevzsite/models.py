from django.db import models
from .choices import TEAM_CHOICES


# Create your models here.
class Program(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    logo = models.ImageField(upload_to='images')

    def _str_(self):
        return self.title

class Geral(models.Model):
    quemSomos = models.CharField(max_length=250)
    visao = models.CharField(max_length=250)
    oqueFazemos = models.CharField(max_length=250)
    logo = models.CharField(max_length=250)

    def __str__(self):
        return self.quemSomos


class Embassador(models.Model):
    name = models.CharField(max_length=250)
    site = models.CharField(max_length=250)
    logo = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email


class Person(models.Model):
    fullname = models.CharField(max_length=100)
    team = models.CharField(choices=TEAM_CHOICES, blank=False,
                            null=False, default='Embassador', max_length=30)
    ocupation = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.fullname
