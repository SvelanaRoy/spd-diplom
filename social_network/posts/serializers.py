from rest_framework import serializers
from posts.models import Post, Comment,Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user','post','text', 'created_at']
        read_only_fields = ['user',]

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user','type','post']
        read_only_fields = ['user',]        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'created_at','image', 'type']
        read_only_fields = ['user',]

class PostDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'created_at','image', 'type']
        read_only_fields = ['user',]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comments'] = list(
            [CommentSerializer(rew).data for rew in Comment.objects.filter(post=instance)]
        )
        representation['likes_count'] = Like.objects.filter(post=instance).count()
        return representation
        
    