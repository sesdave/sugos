from django.contrib import admin
from home.models import Post
from home.models import UserMessage
from home.models import Friend

admin.site.register(Post)
admin.site.register(UserMessage)
admin.site.register(Friend)


# Register your models here.
