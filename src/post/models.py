from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce import HTMLField

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
    #To count the comments
    view_count = models.IntegerField(default = 0)
    #Author field
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    content = HTMLField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=True)
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null= True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null= True)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id' :self.id,
        })

    
    
    def __str__(self):
        return self.title
    
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')
    
class Comment(models.Model):
     user = models.ForeignKey( User, on_delete=models.CASCADE)
     timestamp = models.DateTimeField(auto_now_add=True)
     content = models.TextField()
     post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)

     def __str__(self):
        return self.user.username
    
