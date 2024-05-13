from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
FEEDBACK_OPTIONS = (
    ('L', 'Like'),
    ('D', 'Dislike'),
)

COMMENT_OPTIONS = (
    ('Y', 'Comment'),
    ('N', 'NoComment'),
)

class Post(models.Model):
    user = models.ForeignKey (User,on_delete = models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField (upload_to="photos",null=True)
    type = models.CharField(max_length=1, choices=COMMENT_OPTIONS)


class Like(models.Model):
    user = models.ForeignKey (User,on_delete = models.CASCADE)
    type = models.CharField(max_length=1, choices=FEEDBACK_OPTIONS)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey (User,on_delete = models.CASCADE)
    post = models.ForeignKey (Post, on_delete = models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
