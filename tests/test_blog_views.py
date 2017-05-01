from django.test import TestCase, RequestFactory
from blog.models import *
from blog.views import *


class BlogViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        about_post = Post.objects.create(title='about')
        about_post.save()
        content_post = Post.objects.create(pk=10, title='aa')
        content_post.save()
        pass

    def test_index(self):
        request = self.factory.get('/blog')
        rep = index(request)
        self.assertTrue(rep.status_code, 200)

    def test_about(self):
        request = self.factory.get('/blog/about')
        rep = about(request)
        self.assertTrue(rep.status_code, 200)

    def test_post(self):
        request = self.factory.get('/blog/post/10')
        rep = post_detail(request, 10)
        self.assertTrue(rep.status_code, 200)
