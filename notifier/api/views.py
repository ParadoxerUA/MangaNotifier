from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MangaListSerializer


class MangaListView(APIView):
    serializer = MangaListSerializer()
    def get(self, request):
        return Response(data={"OK!"}, status=200)

    def post(self, request):
        data = request.data
        serializer = MangaListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=201)
