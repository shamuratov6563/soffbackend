from django.shortcuts import render
from .models import *
from . import serializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView, Response
from django.core.paginator import Paginator
from rest_framework.pagination import LimitOffsetPagination



class AdvantageListAPIView(ListAPIView):
    queryset = Advantage.objects.all()
    serializer_class = serializers.AdvantageListSerializer
    # filter_backends = [SearchFilter,DjangoFilterBackend, ]
    # search_fields = ("full_name", )
    # filterset_fields = ("created_at", "status", "amount", )

class AdvantageDetailAPIView(RetrieveAPIView):
    queryset = Advantage.objects.all()
    serializer_class = serializers.AdventageDetailSerializer

class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleListSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend, ]
    pagination_class = LimitOffsetPagination
    search_fields = ("title", )
    filterset_fields = ("category", "author")



class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleDetailSerializer

class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseListSerializer

class CourseDetailAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseDetailSerializer



class ApplicationCreateAPIView(CreateAPIView):
    queryset = ApplicationForm
    serializer_class = serializers.ApplicationCreateSerializer


class CategoryWithCountAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryWithCountSerializer


class AuthorDetailAPIView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    lookup_field = "pk"


class Way2JobAPIView(APIView):

    def get(self, request):
        object = Way2Job.objects.last()
        serializer = serializers.Way2JobSerializer(object)
        return Response(serializer.data)


class GalleryListAPIView(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = serializers.GallerySerializer