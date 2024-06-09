from django.shortcuts import render
from django.views.generic import TemplateView
from pages.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from pages.models import Post
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    