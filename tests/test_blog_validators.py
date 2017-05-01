from django.test import TestCase, RequestFactory
from blog.models import Post
from blog.validators import validate_min_length
from django.core.exceptions import ValidationError


class BlogValidatorsTest(TestCase):
    def test_minlength_validator(self):
        post = Post(title='test')
        self.assertRaises(ValidationError, post.full_clean)
