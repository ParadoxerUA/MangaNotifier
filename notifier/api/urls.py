from django.urls import path
from .views import MangaListView

urlpatterns = [
    path('main/', MangaListView.as_view()),
]