from django.db import models

# Field Type Reference:
# https://docs.djangoproject.com/en/1.11/ref/models/fields/

# Create your models here.
class Family(models.Model):
    ICEContactName = models.CharField(max_length=200)
    ICEContactPhone = models.CharField(max_length=200)

    def children(self):
        """ get list of Clubbers objects that match """
        pass

    def parents(self):
        """ get list of Adults objects with Parent==True that match """
        pass

class Clubber(models.Model):
    Family = models.ForeignKey('Family')
    Club = models.ForeignKey('Club')
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    DOB = models.DateField()

    def age(self):
        """ Figure out age from dob """
        pass

    def __str__(self):
        return ' '.join((self.FirstName, self.LastName))

class Adult(models.Model):
    Family = models.ForeignKey('Family')
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Parent = models.BooleanField()
    Leader = models.BooleanField()

    def __str__(self):
        return ' '.join((self.FirstName, self.LastName))

class Club(models.Model):
    Name = models.CharField(max_length=10)

class Handbook(models.Model):
    Name = models.CharField(max_length=100)
    Club = models.ForeignKey('Club')

class Section(models.Model):
    Name = models.CharField(max_length=100)
    Handbook = models.ForeignKey('Handbook')
