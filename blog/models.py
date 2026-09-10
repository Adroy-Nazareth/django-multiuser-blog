from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
class Tag(models.Model):
    name=models.CharField(max_length=40,unique=True); slug=models.SlugField(max_length=50,unique=True)
    def save(self,*args,**kwargs):
        if not self.slug:self.slug=slugify(self.name)
        return super().save(*args,**kwargs)
    def __str__(self):return self.name
class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='posts')
    title=models.CharField(max_length=180); slug=models.SlugField(max_length=200,unique=True); excerpt=models.TextField(max_length=300); content=models.TextField()
    tags=models.ManyToManyField(Tag,blank=True,related_name='posts'); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True); published=models.BooleanField(default=True)
    class Meta:ordering=['-created_at']
    def save(self,*args,**kwargs):
        if not self.slug:self.slug=slugify(self.title)
        return super().save(*args,**kwargs)
    def get_absolute_url(self):return reverse('post_detail',args=[self.slug])
    def __str__(self):return self.title
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments'); author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comments')
    body=models.TextField(max_length=1000); approved=models.BooleanField(default=False); created_at=models.DateTimeField(auto_now_add=True)
    class Meta:ordering=['created_at']
    def __str__(self):return f'{self.author} on {self.post}'
