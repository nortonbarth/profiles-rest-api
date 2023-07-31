from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Return a list of API features"""
        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            'Gives you the mos control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response(
            {"message":"hello",
            'an_apiview':an_apiview
            }
                        )

# Create your views here.
