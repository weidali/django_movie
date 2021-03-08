from django.urls import path

from .views import *


urlpatterns = [
    path('movie/', MovieListView.as_view()),
    path('movie/<int:pk>/', MovieDetailView.as_view()),

    path('review/', ReviewCreateView.as_view()),

    path('actors/', ActorsListView.as_view()),
    path('actors/<int:pk>', ActorDetailView.as_view()),
]
