from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import User, Blog, Like
from .serializers import (
    UserSerialiazers,
    BlogSerialiazers,
    LikeSerialiazers,
    BlogLikeSerialiazers,
)
from .permission import OnlyBlogOwner
from django.db.models import Count


# ALL USER CRUD Opration
class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialiazers


# All Blog API CRUD Opration
class BlogViewset(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerialiazers
    permission_classes = (
        OnlyBlogOwner,
    )  # Check ['PUT','DELETE','PATCH'] Access in Owner

    # restricted Get based on Private/Public level
    def list(self, request, *args, **kwargs):
        new_query = self.get_queryset().filter(
            user=request.user.id,
            is_private=True,
        )
        public_query = self.get_queryset().filter(is_private=False)
        if new_query.exists():
            queryset = new_query | public_query
        else:
            queryset = public_query
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_private and instance.user.id != request.user.id:
            return Response(
                {"detail": "You don't have permission to view this item."},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


# All Like API CRUD oprations
class LikeViewset(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerialiazers


# Number of Like API
class NumberOfLikeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        like = Like.objects.values("blog").annotate(number_of_like=Count("id"))
        return Response(data=like, status=status.HTTP_200_OK)


# Each Blog How many Like
class BlogwithLikeAPIView(APIView):
    def get(self, request):
        like = Like.objects.all()
        serializer = BlogLikeSerialiazers(like, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
