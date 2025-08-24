from django.shortcuts import render
from rest_framework import generics, viewsets, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response


# Create your views here.

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only the author of a post/comment can edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    # Enable search and ordering
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "content"]  # allow searching posts
    ordering_fields = ["created_at", "updated_at", "title"]  # allow ordering

    def perform_create(self, serializer):
        # Automatically set logged-in user as the author
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # Automatically set logged-in user as the author
        serializer.save(author=self.request.user)


class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  
    serializer_class = PostSerializer

    def get(self, request):
        # Get users that the current user follows
        following_users = request.user.following.all()

        # Get posts from those users, ordered by most recent first
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)