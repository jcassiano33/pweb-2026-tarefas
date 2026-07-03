from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<int:id_post>/", views.posts, name="posts"),
]