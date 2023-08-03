from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import filters, renderers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.renderers import TemplateHTMLRenderer



from . import serializers
from . import models
from . import permissions



class HelloApiView(APIView):
    """Test API view"""

    serializers_class = serializers.HelloSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "profiles_api/base.html"
    def get(self, request, format=None):
        """Return a list of API features"""
        
        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            'Gives you the mos control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response(
            template_name = "profiles_api/base.html"
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
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, requests):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_upadate)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({
            'message':'Hello!',
            'a_viewset':a_viewset,
        })
    
    def create(self, request):
        '''create a new hello message'''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!!!'
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """pk=None getting an object by its ID"""
        return Response ({'http_method':'GET'})
    
    def update(self, request):
        """Handle updating an object"""
        return Response ({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle Partial updating an object"""
        return Response ({'http_method':'PATCH'})    
    
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response ({'http_method':'DELETE'})        
    

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)



class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES