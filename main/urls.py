from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
        path("", views.home, name="home"),
        path("tutorial/", views.tutorial, name="tutorial"),
        path("about/", views.about, name="about"),
]
