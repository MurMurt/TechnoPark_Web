from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='static/user_avatars', null=False,
                               default='static/user_avatars/User_Avatar.png')


class VoteMixIn(models.Model):
    positive_votes = models.ManyToManyField(User, related_name='likes')
    negative_votes = models.ManyToManyField(User, related_name='dislikes')

    def like(self, user):
        self.negative_votes.remove(user)
        self.positive_votes.add(user)

    def dislike(self, user):
        self.positive_votes.remove(user)
        self.negative_votes.add(user)


class Tag(models.Model):
    title = models.CharField(max_length=32, null=False)


class Question(VoteMixIn):
    title = models.CharField(max_length=96, null=False)
    text = models.TextField(max_length=960, null=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    date = models.DateField(auto_now=True)


class Answer(VoteMixIn):
    text = models.TextField(max_length=960)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='author')
    quest = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    date = models.DateField(auto_now=True)
