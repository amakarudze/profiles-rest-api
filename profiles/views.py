from rest_framework.response import Response
from rest_framework.views import APIView


class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete).',
            'Is similar to a traditional Django View.',
            'Gives you the most control over your application logic.',
            'Is mapped manually to URLS.'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
