from django.urls import path

from .views import (
    ListFilmsView,
)

app_name = "main"

urlpatterns = [
    path("list_films", ListFilmsView.as_view(), name="list_films"),
]
