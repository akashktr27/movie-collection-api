from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

@csrf_exempt
def health(request):
    if request.method == 'GET':
        data = {"status": "OK"}
        from django.http import JsonResponse
        return JsonResponse(data, safe=False)

class TokenPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"detail": str(e)}, status=400)

        tokens = serializer.validated_data

        # Return only the access token
        return Response({
            'access': tokens.get('access'),
        })

