# from rest_framework import serializers
# from .models import *
# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Movie
#         fields="__all__"

from rest_framework import serializers
from .models import Movie, Actors

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = '__all__'  # Barcha maydonlarni olish

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)  # Aktyorlar to‘liq ma’lumot shaklida qaytadi
    actors_ids = serializers.PrimaryKeyRelatedField(
        queryset=Actors.objects.all(), many=True, write_only=True
    )  # Yangi aktyorlar qo‘shish uchun

    class Meta:
        model = Movie
        fields = '__all__'  # Barcha maydonlarni qaytarish

    def create(self, validated_data):
        actors_data = validated_data.pop('actors_ids', [])  # Yangi aktyorlar ro‘yxatini olish
        movie = Movie.objects.create(**validated_data)
        movie.actors.set(actors_data)  # ManyToMany bog‘lanishni saqlash
        return movie

    def update(self, instance, validated_data):
        actors_data = validated_data.pop('actors_ids', None)  # Yangilashda aktyorlar bo‘lsa olish
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if actors_data is not None:
            instance.actors.set(actors_data)  # Yangilangan aktyorlar
        instance.save()
        return instance
