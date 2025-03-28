
from rest_framework import serializers
from .models import Movie, Actors

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    actors_ids = serializers.PrimaryKeyRelatedField(
        queryset=Actors.objects.all(), many=True, write_only=True
    )  # Yangi aktyorlar qo‘shish uchun

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        actors_data = validated_data.pop('actors_ids', [])
        # Yangi aktyorlar ro‘yxatini olish
        movie = Movie.objects.create(**validated_data)
        movie.actors.set(actors_data)
        return movie

    def update(self, instance, validated_data):
        actors_data = validated_data.pop('actors_ids', None)
        # Yangilashda aktyorlar bolsa olish
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if actors_data is not None:
            instance.actors.set(actors_data)
        instance.save()
        return instance
