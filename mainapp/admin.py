from django.contrib import admin
from mainapp.models import (Post,Like,DisLikes)
# Register your models here.

admin.site.register(Post)

class LikesAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at']


class DisLikesAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at']


admin.site.register(DisLikes)
admin.site.register(Like)