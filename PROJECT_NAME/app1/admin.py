from django.contrib import admin

# Register your models here.

from .models import User, Post

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','user_name','pwd']



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user','title']