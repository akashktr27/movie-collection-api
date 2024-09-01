from django.http import JsonResponse
from django.conf import settings

class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # If response status code is 404, return custom JSON response
        if response.status_code == 404 and not settings.DEBUG:
            return JsonResponse({
                "error": "Not Found",
                "message": "The requested resource was not found on this server."
            }, status=404)

        return response

from django.utils.deprecation import MiddlewareMixin

class RequestCountMiddleware(MiddlewareMixin):
    request_count = 0  # Class-level variable to store request count

    @classmethod
    def get_count(cls):
        return cls.request_count

    @classmethod
    def reset_count(cls):
        cls.request_count = 0

    def process_request(self, request):
        RequestCountMiddleware.request_count += 1
        print(f"Request count: {RequestCountMiddleware.request_count}")
        request.request_count = RequestCountMiddleware.request_count

