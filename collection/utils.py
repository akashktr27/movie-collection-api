from rest_framework.response import Response
from rest_framework.views import exception_handler
from django.http import Http404
from rest_framework import status
import requests
from requests.auth import HTTPBasicAuth

class ThirdPartyAPIClient:
    def __init__(self, base_url, username, password, max_retries=5):
        self.base_url = base_url
        self.auth = HTTPBasicAuth(username, password)
        self.max_retries = max_retries

    def fetch_page(self, page=1):
        url = f"{self.base_url}?page={page}"
        try:
            for _ in range(self.max_retries):
                print('you win')
                response = requests.get(url, auth=self.auth, verify=False)
                if response.status_code == 200:
                    data = response.json()
                    if 'results' in data:
                        data['data'] = data.pop("results")
                        return data
            else:
                response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data from third-party API: {e}")

def custom_exception_handler(exc, context):
    if isinstance(exc, Http404):
        custom_response_data = {
            'error': 'Not Found',
            'message': 'The requested resource was not found on this server.'
        }
        return Response(custom_response_data, status=status.HTTP_404_NOT_FOUND)
    response = exception_handler(exc, context)

    return response