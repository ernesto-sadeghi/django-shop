from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=255)
    def  __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="blog/",default="blog/default.jpg")
    category = models.ManyToManyField(Categories)
    # tag

    #on_delete=> it asks for deleting or keeping content which user created or not 
    author=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    views_count = models.IntegerField(default=0)
    status= models.BooleanField(default=False)
    published_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    class Meta:
        ordering =["created_date"]
        # verbose_name = "پست"
        # verbose_name_plural = " پست ها"
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog:single",kwargs={"pid":self.id})
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    # approve // spewlling mistake
    approach = models.BooleanField(default=False)
    
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering =["created_date"]
        # verbose_name = "پست"
        # verbose_name_plural = " پست ها"
    def __str__(self):
        return self.subject
 
    