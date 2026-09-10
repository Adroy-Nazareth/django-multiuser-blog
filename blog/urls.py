from django.contrib.syndication.views import Feed
from django.urls import path
from .models import Post
from .views import home,post_create,post_detail,post_edit
class LatestPostsFeed(Feed):
    title='Django Multiuser Blog';link='/';description='Latest posts from the community blog.'
    def items(self):return Post.objects.filter(published=True).select_related('author')[:20]
    def item_title(self,item):return item.title
    def item_description(self,item):return item.excerpt
    def item_link(self,item):return item.get_absolute_url()
    def item_author_name(self,item):return item.author.username
urlpatterns=[path('',home,name='home'),path('posts/new/',post_create,name='post_create'),path('posts/<slug:slug>/',post_detail,name='post_detail'),path('posts/<slug:slug>/edit/',post_edit,name='post_edit'),path('feed/',LatestPostsFeed(),name='post_feed')]
