from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Book


class IndexView(generic.ListView):
    model = Book
    template_name = 'books/index.html'

class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'
