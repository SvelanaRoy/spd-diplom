from django.shortcuts import render
from django.http import Http404
from rest_framework.viewsets import ModelViewSet

from posts.models import Post, Like, Comment
from posts.permissions import IsOwnerOrReadOnlyPost
from posts.permissions import IsAuthenticatedOrReadOnlyComment,IsAuthenticatedOrReadOnlyLike
from posts.serializers import PostSerializer,PostDetailsSerializer
from posts.serializers import CommentSerializer,LikeSerializer
from rest_framework.permissions import IsAuthenticated


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostDetailsSerializer
    permission_classes = [IsOwnerOrReadOnlyPost]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#class CommentViewSet(ModelViewSet):
#    queryset = Comment.objects.all()
#    serializer_class = CommentSerializer
#    permission_classes = [IsAuthenticatedOrReadOnlyComment]
#    def perform_create(self, serializer):
#        serializer.save(user=self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnlyComment]
    def perform_create(self, serializer):
        postid = Comment.objects.values_list("post", flat=True)
        for p in postid:
            somepost = Post.objects.get(id=p)
            if somepost.type == "Y":
                serializer.save(user=self.request.user)
                

class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnlyLike]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)                 
