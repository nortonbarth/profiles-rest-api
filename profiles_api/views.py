from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

class HelloApiView(APIView):
    """Test API view"""

    serializers_class = serializers.HelloSerializer

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

    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request, pk=None):
        """Handle and update an object"""
        return Response({'method':"PUT"})
        
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':"PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':"DELETE"})

# Create your views here.
