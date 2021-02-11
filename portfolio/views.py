from rest_framework import serializers, status
from rest_framework.views import APIView
from portfolio.models import Blog, Work
from portfolio.serializers import ContactSerializer, WorkSerializer, BlogSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny
# Create your views here.
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.status import HTTP_200_OK
from rest_framework.filters import SearchFilter, OrderingFilter


class ContactView(CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save()


class WorkListView(ListAPIView):
    serializer_class = WorkSerializer
    permission_classes = (AllowAny,)
    queryset = Work.objects.all()

    def get_queryset(self):
        return Work.objects.all().order_by('-date')


class ProductFilterListView(ListAPIView):
    serializer_class = WorkSerializer
    permission_classes = (AllowAny,)
    queryset = Work.objects.all()

    def get_queryset(self):
        return Work.objects.filter(category="Product Design").order_by('-date')


class SearchView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def get(self, request, *args, **kwargs):
        query = request.query_params.get("search", None)
        if query is None:
            print(query)
            return Response({"message": "No item in search"}, status=HTTP_200_OK)
        blog = Blog.objects.all()
        print(query)
        queryset = blog.filter(Q(title__icontains=query) | Q(
            description__icontains=query) | Q(post__icontains=query))
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)


class TagsView(ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        slug = request.query_params.get('slug', None)
        print(slug)
        if slug is None:
            return Response({"message": "no blog"}, status=HTTP_400_BAD_REQUEST)

        post = get_object_or_404(Blog, slug=slug)
        tags = post.tags.similar_objects()[:2]
        serializer = BlogSerializer(tags, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class FlyersFilterListView(ListAPIView):
    serializer_class = WorkSerializer
    permission_classes = (AllowAny,)
    queryset = Work.objects.all()

    def get_queryset(self):
        return Work.objects.filter(category="Flyers").order_by('-date')


class BrandFilterListView(ListAPIView):
    serializer_class = WorkSerializer
    permission_classes = (AllowAny,)
    queryset = Work.objects.all()

    def get_queryset(self):
        return Work.objects.filter(category="Branding Identity").order_by('-date')


class PackageFilterListView(ListAPIView):
    serializer_class = WorkSerializer
    permission_classes = (AllowAny,)
    queryset = Work.objects.all()

    def get_queryset(self):
        return Work.objects.filter(category="Package").order_by('-date')


class CampaignFilterListView(ListAPIView):
    serializer_class = WorkSerializer
    permission_classes = (AllowAny,)
    queryset = Work.objects.all()

    def get_queryset(self):
        return Work.objects.filter(category="Campaign").order_by('-date')


class CommunicationFilterListView(ListAPIView):
    serializer_class = WorkSerializer
    permission_classes = (AllowAny,)
    queryset = Work.objects.all()

    def get_queryset(self):
        return Work.objects.filter(category="Communication").order_by('-date')


class BlogListView(ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)
    queryset = Blog.objects.all()

    def get_queryset(self):
        return Blog.objects.all().order_by('-date')


class BlogDetailView(RetrieveAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)
    queryset = Blog.objects.all()
    lookup_field = 'slug'
