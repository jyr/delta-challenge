from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apis.search.api.news.serializers import NewsSerializer

class NewsEndpoint(APIView):

    def post(self, request):
        """
        post:
        Return news by keywords
        """
        serializer =  NewsSerializer(data=request.data)

        if serializer.is_valid():

            try:
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
            except:
                raise Http404

        return Response(
            {"error":serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
