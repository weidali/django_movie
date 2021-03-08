from rest_framework import serializers, generics
from .models import *


class ActorsListSerializer(serializers.ModelSerializer):
    """Films list"""
    class Meta:
        model = Actor
        fields = ('id', 'name', 'image', )


class ActorDetailSerializer(serializers.ModelSerializer):
    """Films list"""
    class Meta:
        model = Actor
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    """Films list"""
    class Meta:
        model = Movie
        fields = ('id', 'title', 'tagline', 'country', 'category',)


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class FilterReviewListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super(FilterReviewListSerializer, self).to_representation(data)


class RecursiveSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ReviewSerializer(serializers.ModelSerializer):
    child = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ('name', 'email', 'text', 'child',)


class MovieDetailSerializer(serializers.ModelSerializer):
    """Film detail"""
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    directors = ActorsListSerializer(read_only=True, many=True)
    actors = ActorsListSerializer(read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ('draft',)
