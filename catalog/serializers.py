from .models import User, Blog, Like
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


# User Serialiazers
class UserSerialiazers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    # String to convert in password Formate.
    def validate(self, attrs):
        attrs["password"] = make_password(attrs.get("password"))
        return attrs


# Blog Serialiazers
class BlogSerialiazers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


# Like Serialiazers
class LikeSerialiazers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


# In single Query both blog and like data
class BlogLikeSerialiazers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
        depth = 1
