from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class UserMessage(models.Model):
    sent_from= models.ForeignKey(User, on_delete=models.CASCADE, related_name='own_message')
    to_who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='other_message')
    message=models.CharField(max_length=500)
    time_sent=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sent_from.username


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)