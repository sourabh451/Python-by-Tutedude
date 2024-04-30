from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from helloworld.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post
from rest_framework.permissions import IsAuthenticated
from helloworld.permissions import IsPostPossessor
# Create your views here.

class HelloWorldView(APIView):

    def get(self,request):
        return Response({'message':'Hello world!'})

class PostView(ModelViewSet):

    permission_classes = [IsAuthenticated, IsPostPossessor]

    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(created_by = self.request.user)