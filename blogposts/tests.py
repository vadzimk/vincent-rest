from django.contrib.auth.models import User
from django.test import TestCase

from blogposts.models import BlogPost


# Create your tests here.


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create user
        user = User.objects.create_user(
            username='testuser',
            password='abc'
        )
        user.save()

        # create blogpost
        blogpost = BlogPost.objects.create(
            author=user,
            title='Blog title',
            body='body content'
        )
        blogpost.save()

    def test_model_content(self):
        post = BlogPost.objects.get(id=1)
        self.assertEqual(str(post.author), 'testuser')
        self.assertEqual(str(post.title), 'Blog title')
        self.assertEqual(str(post.body), 'body content')