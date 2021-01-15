from django.urls import path
from .views import MangaListView, AuthView

urlpatterns = [
    path('main/', MangaListView.as_view()),
    path('register', AuthView.as_view()),
]