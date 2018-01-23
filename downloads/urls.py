from django.urls import path
from . import views


app_name = "downloads"
urlpatterns = [
        path("", views.list, name="index"),
]
