from rest_framework import serializers
from .models import *


class MovieListSerializer(serializers.ModelSerializer):
    """Films list"""
    class Meta:
        model = Movie
        fields = ('title', 'tagline', 'country', 'category',)


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('name', 'email', 'text', 'parent',)


class MovieDetailSerializer(serializers.ModelSerializer):
    """Film detail"""
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    directors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ('draft',)
