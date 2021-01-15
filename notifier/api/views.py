from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MangaListSerializer, UserSerializer


class MangaListView(APIView):

    def get(self, request):

        return Response(data={"OK!"}, status=200)

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
