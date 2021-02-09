from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from .models import User, MangaList
from .serializers import MangaListSerializer, UserSerializer


class MangaListView(APIView):

    def get(self, request):
        manga_list = MangaList.objects.all()
        serializer = MangaListSerializer(manga_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = MangaListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=201)


class AuthView(APIView):

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=201)


class RegisterView(APIView):

    def post(self, request):
        data = request.data
        user = User.objects.filter(email=data["email"])
        if user:
            if check_password(data["password"], user.password):
                response = Response(data="You've successfully loged in")
                response.set_cookie('user', user.username)
                return response

        return Response(data="Wrong credentials", status=400)
