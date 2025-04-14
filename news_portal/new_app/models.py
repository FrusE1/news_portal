from email.policy import default

from django.db import models
from django.contrib.auth.models import User

from new_app.resources import POST_TYPE, news


# from news_portal.new_app.resources import POST_TYPE, news


class Author(models.Model):
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def update_rating(self):
        rating_posts = Post.objects.filter(author = self).values_list('rating', flat=True)
        rating_comments = Comment.objects.filter(user = self.user).values_list('rating', flat=True)
        rating_post_comments = Comment.objects.filter(post__author = self).values_list('rating', flat=True)
        self.rating = sum(rating_posts) * 3 + sum(rating_comments) + sum(rating_post_comments)
        self.save()

class Category(models.Model):
    category = models.CharField(unique = True)

class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    rating = models.IntegerField(default = 0)
    type = models.CharField(max_length = 2, choices = POST_TYPE, default = news)
    data_create = models.DateField(auto_now_add = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        if len(self.text) > 124:
            return self.text[:124] + '...'
        else:
            return self.text

class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField()
    datetime_create = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default = 0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()