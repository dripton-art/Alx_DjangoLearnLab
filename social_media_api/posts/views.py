from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed(request):
    """
    Returns a feed of posts from users the current user follows.
    Ordered by creation date (most recent first).
    """
    user = request.user
    following_users = user.following.all()  # users the current user follows
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    
    # Minimal representation without serializer
    feed_data = [
        {
            "id": post.id,
            "author": post.author.username,
            "content": post.content,
            "created_at": post.created_at
        } for post in posts
    ]
    
    return Response(feed_data)