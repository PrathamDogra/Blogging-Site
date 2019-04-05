from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    #To add the time of post creation
    timestamp = models.DateTimeField(auto_now_add=True)
    #To count the number of counts
    comment_count = models.IntegerField(default = 0)
    #Author field
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()

    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=True)


    def __str__(self):
        return self.title

