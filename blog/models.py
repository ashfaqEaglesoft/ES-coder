from enum import auto
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField 

# from django.contrib.auth.models import User
# from django.conf import settings 
# from blog.models import post
# from django.utils import timezone


# Create your models here.
class post(models.Model):
    post_title=models.CharField(max_length=200)
    post_publish_date=models.DateField()
    post_author=models.CharField(max_length=50,default="Admin")
    post_slug=models.CharField(max_length=150,default="")
    post_category=models.CharField(max_length=150,default="programmer")
    # post_image=models.ImageField(/media)
    post_content=models.CharField(max_length=5000)
    def __str__(self):
        return self.post_title

class blogComment(models.Model):
    comment=models.CharField(max_length=5000)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    # user=models.ForeignKey(User,on_delete=CASCADE)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    # post = models.ForeignKey(post,on_delete=models.CASCADE)
    # timestamp=models.TimeField(default=timezone.now)
    def __str__(self):
        return f"comment: {self.comment} "