from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
        path("", views.newsPostList, name="index"),
        path("post/<int:news_post_id>", views.newsPost, name="post"),
]
