from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    
    def __str__(self):
        return "{}, {}".format(self.first_name[0], self.surname)

@python_2_unicode_compatible
class AgeRecommendation(models.Model):
    recommendation = models.CharField(max_length=20)

    def __str__(self):
        return self.recommendation

@python_2_unicode_compatible
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default="")
    author = models.ForeignKey(Author)
    pub_date = models.DateTimeField('date published')
    age_recommendation = models.ForeignKey(AgeRecommendation)
    genre = models.ForeignKey(Genre)
    cover_image = models.ImageField(null=True, upload_to="covers/")

    def __str__(self):
        return self.title
    
    
