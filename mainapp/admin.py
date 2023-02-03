from django.contrib import admin
from mainapp.models import (User,Post)
# Register your models here.

admin.site.register(User)
admin.site.register(Post)