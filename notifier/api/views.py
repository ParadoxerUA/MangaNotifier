from rest_framework.views import APIView
from rest_framework.response import Response


class MangaListView(APIView):

    def get(self, request):
        return Response(data={"OK!"}, status=200)
