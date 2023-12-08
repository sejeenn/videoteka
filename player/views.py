from django.shortcuts import render
from django.views.generic import ListView

from .models import Video


class ListFilmsView(ListView):
    template_name = 'player/list_films.html'
    context_object_name = "list_films"
    queryset = Video.objects.all()
