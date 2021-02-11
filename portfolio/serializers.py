
from portfolio.models import Contact, Blog, Work
from rest_framework import serializers
from django.contrib.auth.models import User
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer


class UserInfo(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            "name",
            "location",
            "email",
            "message"
        )


class BlogSerializer(TaggitSerializer, serializers.ModelSerializer):

    username = serializers.SerializerMethodField()
    tags = TagListSerializerField()

    class Meta:
        model = Blog
        fields = (
            "title",
            "description",
            "post",
            "image",
            "author",
            "facebook",
            "twitter",
            "linkedin",
            "date",
            "slug",
            'username',
            'tags',

        )

    def get_username(self, obj):
        return UserInfo(obj.author).data


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = (
            "title",
            "brief",
            "challenges",
            "category",
            "approach",
            "image",
            "image1",
            "image2",
            "image3",
            "image4",
            "image5",
            "image6",
            "date",
            "slug"
        )
