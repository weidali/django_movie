from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *
from .service import *


class MovieListView(generics.ListAPIView):
    """Input films list"""
    serializer_class = MovieListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter

    def get_queryset(self):
        movies = Movie.objects.filter(draft=False)
        return movies


class MovieDetailView(generics.RetrieveAPIView):
    """Input film's detail"""
    queryset = Movie.objects.filter(draft=False)
    serializer_class = MovieDetailSerializer


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer


class ActorsListView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorsListSerializer


class ActorDetailView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer
