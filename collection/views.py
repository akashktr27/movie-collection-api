import os
from django.http import JsonResponse
from django.views import View
from .middleware import RequestCountMiddleware
from rest_framework_simplejwt.authentication import JWTAuthentication
from requests.auth import HTTPBasicAuth
from rest_framework.views import APIView
from .utils import *
from .models import *
from .serializers import *
from collections import Counter
# Create your views here.
class MovieView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        url = os.getenv("url")
        username = os.getenv("username")
        password = os.getenv("password")
        results = []
        page = request.query_params.get('page', 1)
        try:
            api_client = ThirdPartyAPIClient(base_url=url, username=username, password=password)
            data = api_client.fetch_page(page=page)
            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({
                "error": "An error occured while trying to fetch",
                "details": str(e)
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CollectionView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        objs = Collection.objects.all()
        print(objs)
        snip_obj = CollectionSerializer(objs, many=True)
        data = {
            "collections": snip_obj.data,
            "favourite_genres": self.favourite_genres(objs)
        }
        output = {
            "is_success": True,
            "data": data
        }
        return Response(output)

    def post(self, request, format=None):
        snip_obj = CollectionSerializer(data=request.data)
        if snip_obj.is_valid():
            snip_obj.save()
            return Response(snip_obj.data.get('uuid'), status=status.HTTP_201_CREATED)
        return Response(snip_obj.errors, status=status.HTTP_400_BAD_REQUEST)


    def favourite_genres(self, objs):
        all_genres = [genre for obj in objs for genre in obj.movies.values_list('genres', flat=True)]
        genre_counts = Counter(all_genres)
        top_3_genres = dict(genre_counts.most_common(3))

        return list(top_3_genres.keys())

class Collection_detail(APIView):
    authentication_classes = [JWTAuthentication]
    def get_object(self, uuid):
        try:
            obj = Collection.objects.get(uuid=uuid)
            return obj
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, uuid):
        print('here')
        obj = self.get_object(uuid)
        print(obj)
        snip_obj = CollectionSerializer(obj,  detail=True)
        return Response(snip_obj.data)

    def put(self, request, uuid):
        obj = self.get_object(uuid)
        print(request.data)
        snip_obj = CollectionSerializer(obj, data=request.data, detail=True )
        if snip_obj.is_valid():
            snip_obj.save()
            return Response(snip_obj.data)
        return Response(snip_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        obj = self.get_object(uuid)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RequestCountView(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        count = RequestCountMiddleware.get_count()
        return JsonResponse({"request_count": count})

    def post(self, request):
        RequestCountMiddleware.reset_count()
        return JsonResponse({"message": "Request count reset to 0", "request_count": 0})

