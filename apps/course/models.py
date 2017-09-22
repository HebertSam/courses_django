from __future__ import unicode_literals

from django.db import models


# Create your models here.
class courseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['name']) < 5:
            errors['name'] = 'Invalid course name please try again'
        if len(postData['description']) < 15:
            errors['desc'] = 'Invalid description please try again'
        return errors




class courses(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = courseManager()