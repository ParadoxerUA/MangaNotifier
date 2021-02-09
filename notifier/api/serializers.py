from rest_framework import serializers
from .models import MangaList, User
from django.contrib.auth.hashers import make_password


class MangaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaList
        # TODO: add mixin instead of passing user to serializer
        fields = ['name', 'url', 'updated', 'user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        user = super().create(validated_data)
        user.save()
        return user
