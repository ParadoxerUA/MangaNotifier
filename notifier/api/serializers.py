from rest_framework import serializers
from .models import MangaList


class MangaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaList
        fields = ['name', 'url', 'updated']