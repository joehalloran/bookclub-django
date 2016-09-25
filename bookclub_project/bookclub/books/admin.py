from django.contrib import admin

from .models import Author, AgeRecommendation, Genre, Book

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(AgeRecommendation)
