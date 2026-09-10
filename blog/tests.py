from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Comment,Post
class BlogTests(TestCase):
    def setUp(self):
        self.user=User.objects.create_user('alice',password='StrongPass123!')
        self.post=Post.objects.create(author=self.user,title='Test Post',slug='test-post',excerpt='Hello',content='Body')
    def test_home_lists_post(self):
        self.assertContains(self.client.get(reverse('home')),'Test Post')
    def test_registration_and_login(self):
        r=self.client.post(reverse('register'),{'username':'bob','email':'b@example.com','password1':'StrongPass123!','password2':'StrongPass123!'})
        self.assertRedirects(r,reverse('home'))
    def test_comment_requires_approval(self):
        self.client.login(username='alice',password='StrongPass123!');self.client.post(self.post.get_absolute_url(),{'body':'Nice post'})
        self.assertEqual(Comment.objects.count(),1);self.assertFalse(Comment.objects.first().approved)
