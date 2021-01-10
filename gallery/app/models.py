from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=60)

    def __str__(self):
        '''
        A string representation
        '''
        return self.location_name

    def save_location(self):
        '''
        A method that saves the location name
        '''
        return self.save()

    @classmethod
    def delete_location(cls, id):
        return cls.objects.filter(id = id).delete()

